from django.contrib import admin
from .models import Client


# Register your models here.

class AdminClient(admin.ModelAdmin):
    list_display = ['client', 'score']
    list_display_links = ['client']
    list_editable = ['score']


admin.site.register(Client, AdminClient)
