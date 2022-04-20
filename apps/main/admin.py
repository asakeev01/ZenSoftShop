from django.contrib import admin

from rest_framework.filters import SearchFilter

from .models import *
from .forms import *


class AdvantageAdmin(admin.ModelAdmin):
    form = AdvantageForm


class HeaderAdmin(admin.ModelAdmin):
    form = HeaderForm

class RequestAdmin(admin.ModelAdmin):
    list_filter = ('called',)
    filter_backends = [SearchFilter]
    search_fields = ['name', 'number']


admin.site.register(Slider)
admin.site.register(SliderImage)
admin.site.register(Advantage, AdvantageAdmin)
admin.site.register(FAQImage)
admin.site.register(FAQ)
admin.site.register(Header, HeaderAdmin)
admin.site.register(Footer)
admin.site.register(Public)
admin.site.register(Url)
admin.site.register(Request, RequestAdmin)
