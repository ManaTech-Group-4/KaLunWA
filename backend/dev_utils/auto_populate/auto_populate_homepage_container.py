from kalunwa.content.models import (
    Jumbotron,
    Event,
    Project,
)
from kalunwa.page_containers.models import (
    PageContainedProject,
    PageContainer,
    PageContainedJumbotron,
    PageContainedEvent,
) 


homepage = PageContainer.objects.create(name='homepage')

# jumbotrons from autopopulate homepage, might merge though
for _ in range(1,6): # 1- 5
    PageContainedJumbotron.objects.create(
        container=homepage,
        jumbotron= Jumbotron.objects.get(pk=_),
        section_order= _,
        )

print('contain homepage jumbotrons')

for _ in range(1,4): # 1- 5
    PageContainedEvent.objects.create(
        container=homepage,
        event= Event.objects.get(pk=_),
        section_order= _,
        )
print('contain homepage events')

for _ in range(1,4): # 1- 5
    PageContainedProject.objects.create(
        container=homepage,
        project= Project.objects.get(pk=_),
        section_order= _,
        )
print('contain homepage projects')

# exec(open("dev_utils/auto_populate/auto_populate_homepage_container.py").read())