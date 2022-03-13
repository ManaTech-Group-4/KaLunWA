from django.contrib import admin
from kalunwa.content.models import Image, Tag, Jumbotron, Announcement, Event
# Register your models here.
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Jumbotron)
admin.site.register(Announcement)
admin.site.register(Event)