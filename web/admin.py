from django.contrib import admin

from .models import Contact
from .models import Sector
from .models import Update


# Register your models here.

admin.site.register(Contact)
admin.site.register(Update)


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ("title",)
