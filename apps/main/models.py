from django.db import models

from ckeditor.fields import RichTextField


TYPES = (
    ('Number', 'Number'),
    ('Mail', 'Mail'),
    ('Telegram', 'Telegram'),
    ('Instagram', 'Instagram'),
    ('Whatsapp', 'Whatsapp')
)


class Slider(models.Model):
    pass


class SliderImage(models.Model):
    slider = models.ForeignKey(Slider, on_delete=models.CASCADE, related_name='slider_images')
    image = models.ImageField(upload_to='sliderImage')


class Advantage(models.Model):
    image = models.ImageField(upload_to='advantageImage')
    header = models.CharField(max_length=55)
    description = models.CharField(max_length=255)


class FAQImage(models.Model):
    image = models.ImageField(upload_to='faqImage')

    class Meta:
        verbose_name = 'FAQImage'
        verbose_name_plural = 'FAQImage'


class FAQ(models.Model):
    image = models.ForeignKey(FAQImage, on_delete=models.CASCADE, related_name='faq')
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'


class Header(models.Model):
    logo = models.ImageField(upload_to='headerImage')
    text = models.CharField(max_length=255)
    phone_num = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Header'
        verbose_name_plural = 'Header'


class Footer(models.Model):
    header = models.ForeignKey(Header, on_delete=models.CASCADE, related_name='footer')
    text = models.CharField(max_length=255)
    type = models.CharField(choices=TYPES, max_length=255)
    link = models.URLField(max_length=255, blank=True)

    def clean(self):
        if self.type == "Whatsapp":
            self.link = "https://wa.me/" + self.text
        elif self.type == "Mail":
            self.link = "https://mailto/" + self.text
        elif self.type == "Telegram":
            self.link = "https://telegram.me/" + self.text
        elif self.type == "Instagram":
            self.link = "https://www.instagram.com"
        elif self.type == "Number":
            self.link = "tel:" + self.text


class Public(models.Model):
    header = models.CharField(max_length=55)
    description = RichTextField()


class Url(models.Model):
    whatsapp = models.URLField(max_length=255)
    telegram = models.URLField(max_length=255)


class Request(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    back_call = models.BooleanField()
    called = models.BooleanField(default=False)
