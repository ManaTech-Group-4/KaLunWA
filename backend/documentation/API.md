# API's
### homepage
url pattern | url configuration location | [base-name]+[type]| 
|:---|:--------------------------:|:-----------:|
/api/                       |rest_framework.routers.view                |api-root|
/api/homepage/events/       |kalunwa.content.views.HomepageViewSet      |homepage-events|
/api/homepage/jumbotrons/   |kalunwa.content.views.HomepageViewSet      |homepage-jumbotrons|
/api/homepage/news/         |kalunwa.content.views.HomepageViewSet      |homepage-news|
/api/homepage/projects/     |kalunwa.content.views.HomepageViewSet      |homepage-projects|
<br>
---
<br>

### about us
url pattern | url configuration location | [base-name]+[type]|
|:---|:--------------------------:|:-----------:|
/api/about-us/total_members/|kalunwa.content.views.AboutUsViewSet       |about-us-total-members|
<br>
---
<br>

### content
url pattern | url configuration location | [base-name]+[type]|
|:---|:--------------------------:|:-----------:|
/api/announcements/         |kalunwa.content.views.AnnouncementViewSet  |announcement-list|
/api/announcements/\<pk>/   |kalunwa.content.views.AnnouncementViewSet  |announcement-detail|
/api/events/                |kalunwa.content.views.EventViewSet         |event-list|
/api/events/\<pk>/          |kalunwa.content.views.EventViewSet         |event-detail|
/api/projects/              |kalunwa.content.views.ProjectViewSet       |project-list|
/api/projects/\<pk>/         |kalunwa.content.views.ProjectViewSet       |project-detail|
/api/news/                  |kalunwa.content.views.NewsViewSet          |news-list|
/api/news/\<pk>/             |kalunwa.content.views.NewsViewSet          |news-detail|
/api/jumbotrons/            |kalunwa.content.views.JumbotronViewSet     |jumbotron-list|
/api/jumbotrons/\<pk>/      |kalunwa.content.views.JumbotronViewSet     |jumbotron-detail|
/api/images/\<pk>/          |kalunwa.content.views.ImageViewSet         |image-detail|
/media/\<path>              |django.views.static.serve

<br>

> Install `django-extensions` and make this command to see full list of url paths (django admin, data formats, etc.):

```powershell
 python manage.py shell -c 'from django.core.management import call_command; from django_extensions.management.commands.show_urls import Command; call_command(Command())'
 ```

updated: *3/18/22 8:41 AM*