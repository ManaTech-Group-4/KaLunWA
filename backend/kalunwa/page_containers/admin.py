from django.contrib import admin

from .models import PageContainedJumbotron, PageContainer

# Register your models here.

admin.site.register(PageContainer)
admin.site.register(PageContainedJumbotron)