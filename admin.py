from mezzanine.pages.admin import PageAdmin
from django.contrib.gis import admin
from .models import NewGenericResource

admin.site.register(NewGenericResource, PageAdmin)
