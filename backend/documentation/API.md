# API's
url pattern | url configuration location | [base-name]+[type]| extra des|
|:---|:--------------------------:|:-----------:|--------------:|
|/api/ |  rest_framework.routers.view|    api-root|
|/api/announcements/| kalunwa.content.views.AnnouncementViewSet| announcement-list
/api/announcements/\<pk>/| kalunwa.content.views.AnnouncementViewSet       |announcement-detail
/api/events/ |kalunwa.content.views.EventViewSet |     event-list|
/api/events/\<pk>/|       kalunwa.content.views.EventViewSet |     event-detail
/api/homepage/events/|   kalunwa.content.views.HomepageViewSet|   homepage-events
/api/homepage/jumbotrons/|       kalunwa.content.views.HomepageViewSet   |homepage-jumbotrons
/api/images/\<pk>/|kalunwa.content.views.ImageViewSet| image-detail|
/api/jumbotrons/ |kalunwa.content.views.JumbotronViewSet|  jumbotron-list
/api/jumbotrons/\<pk>/|   kalunwa.content.views.JumbotronViewSet|  jumbotron-detail
/media/\<path>|   django.views.static.serve

<br>

> Install `django-extensions` and make this command to see full list of url paths (django admin, data formats, etc.):

```powershell
 python manage.py shell -c 'from django.core.management import call_command; from django_extensions.management.commands.show_urls import Command; call_command(Command())'
 ```

updated: *3/17/22 10:23 AM*