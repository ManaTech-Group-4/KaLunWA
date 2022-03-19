from django.contrib import admin
from kalunwa.content.models import Image, Tag, Jumbotron, Announcement, Event, Project, News
# Register your models here.
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Jumbotron)
admin.site.register(Event)
admin.site.register(Project)
admin.site.register(News)
admin.site.register(Announcement)

