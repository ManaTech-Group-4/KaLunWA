from django.contrib import admin
from kalunwa.content.models import Contributor, Image, Tag, Jumbotron, Announcement, Event, Project, News
from kalunwa.content.models import Demographics, CampPage, OrgLeader, Commissioner, CampLeader, CabinOfficer

# Register your models here.
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Jumbotron)
admin.site.register(Event)
admin.site.register(Project)
admin.site.register(News)
admin.site.register(Announcement)
admin.site.register(Demographics)
admin.site.register(CampPage)
admin.site.register(OrgLeader)
admin.site.register(Commissioner)
admin.site.register(CampLeader)
admin.site.register(CabinOfficer)
admin.site.register(Contributor)


