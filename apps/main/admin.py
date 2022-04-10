from django.contrib import admin

from .models import *
from .forms import *


class AdvantageAdmin(admin.ModelAdmin):
    form = AdvantageForm

admin.site.register(Slider)
admin.site.register(SliderImage)
admin.site.register(Advantage, AdvantageAdmin)
