from django.contrib import admin

# Register your models here.
from .models import Display_item
class Category_name(admin.ModelAdmin):
    list_display=["name"]

admin.site.register(Display_item,Category_name)
