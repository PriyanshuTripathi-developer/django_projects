from django.contrib import admin
from .models import Herb

admin.site.register(Herb)
class HerbAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name')
    search_fields = ('name', 'scientific_name', 'ailments')