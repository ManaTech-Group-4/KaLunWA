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

def to_expected_iso_format(date: datetime)->str:
    """
    convert to iso-8061; how date is serialized by default        
    """
    date = date.isoformat()
    # +00:00 marks for UTC, which Z also represents (used by serializer as well)
    return str(date).replace('+00:00', 'Z')

HOMEPAGE_JUMBOTRON_URL = '/api/jumbotrons/?expand=image&omit=created_at,updated_at,image.id&is_featured=True&query_limit=5'
HOMEPAGE_EVENT_URL = '/api/events/?expand=image&fields=id,title,image.image&is_featured=True&query_limit=3'
HOMEPAGE_PROJECT_URL = '/api/projects/?expand=image&fields=id,title,image.image&is_featured=True&query_limit=3'
HOMEPAGE_NEWS_URL = '/api/news/?expand=image&omit=created_at,updated_at,image.id&query_limit=3'

ABOUT_US_CAMP_URL = '/api/camps/?expand=image&omit=created_at,updated_at&name__in=Suba,Zero%20Waste,Baybayon,Lasang'
ABOUT_US_TOTAL_MEMBERS = '/api/demographics/total-members/'
ABOUT_US_LEADERS = '/api/orgleaders/?expand=image&fields=id,image&position=ExeComm'
EVENT_DETAIL_GALLERY_LIMIT = '/api/events/?expand=gallery,contributors&query_limit_gallery=10' # expected fields for detail
EVENT_DETAIL_CONTRIBUTORS = '/api/events/?expand=contributors.image'
PROJECT_DETAIL_GALLERY_LIMIT = '/api/projects/?expand=gallery,contributors&query_limit_gallery=10'
PROJECT_DETAIL_CONTRIBUTORS = '/api/projects/?expand=contributors.image'
CAMP_DETAIL_GALLERY_LIMIT = '/api/camps/?expand=gallery&query_limit_gallery=10'

ANNOUNCEMENT_LATEST_ONE = '/api/announcements/?omit=created_at,updated_at&query_limit=1'
NEWS_LATEST_ONE = '/api/news/?omit=created_at,updated_at&query_limit=1'