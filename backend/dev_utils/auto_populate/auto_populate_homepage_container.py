from kalunwa.content.models import Jumbotron
from kalunwa.page_containers.models import (
    PageContainer,
    PageContainedJumbotron,
) 


homepage = PageContainer.objects.create(name='homepage')

# jumbotrons from autopopulate homepage, might merge though
for _ in range(1,6): # 1- 5
    PageContainedJumbotron.objects.create(
        container=homepage,
        jumbotron= Jumbotron.objects.get(pk=_),
        section_order= _,
        )

# add related jumbotrons to display


# exec(open("dev_utils/auto_populate/auto_populate_homepage_container.py").read())