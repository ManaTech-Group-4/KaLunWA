from datetime import datetime
from io import BytesIO
import PIL.Image
from django.core.files.images import ImageFile
from kalunwa.content.models import CampEnum

def get_test_image_file(filename="test.jpg", colour=0, size=(1, 1))->ImageFile:
    f = BytesIO()
    image = PIL.Image.new('1', size, colour)
    image.save(f, "png")
    return ImageFile(f, name=filename)

def get_expected_image_url(file_name, request):
    """
    build complete url 
    request.scheme -> http
    request.get_host() -> testserver        
    self.image.image.name [file name]->  images/content/test_U5U97df.jpg
    """
    return f'{request.scheme}://{request.get_host()}/media/{file_name}'

def to_formal_mdy(date:datetime)->str:
    return f'{date.strftime("%B")} {date.day}, {date.year}'    

def get_camp_value_via_label(label):
    if label == CampEnum.BAYBAYON.label:
        return CampEnum.BAYBAYON.value
    if label == CampEnum.SUBA.label:
        return CampEnum.SUBA.value
    if label == CampEnum.LASANG.label:
        return CampEnum.LASANG.value
    if label == CampEnum.ZEROWASTE.label:
        return CampEnum.ZEROWASTE.value
    if label == CampEnum.GENERAL.label:
        return CampEnum.GENERAL.value

    return None

HOMEPAGE_JUMBOTRON_URL = '/api/jumbotrons/?expand=image&omit=created_at,updated_at,image.id&is_featured=True&query_limit=5'
HOMEPAGE_EVENT_URL = '/api/events/?expand=image&fields=id,title,image.image&is_featured=True&query_limit=3'
HOMEPAGE_PROJECT_URL = '/api/projects/?expand=image&fields=id,title,image.image&is_featured=True&query_limit=3'
HOMEPAGE_NEWS_URL = '/api/news/?expand=image&omit=created_at,updated_at,image.id&query_limit=3'

ABOUT_US_CAMP_URL = '/api/camps/?expand=image&omit=created_at,updated_at&one_each=True'
ABOUT_US_TOTAL_MEMBERS = '/api/demographics/total-members/'
ABOUT_US_LEADERS = '/api/orgleaders/?expand=image&fields=id,image&position=execomm'