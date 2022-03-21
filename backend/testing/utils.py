from io import BytesIO
import PIL.Image
from django.core.files.images import ImageFile


def get_test_image_file(filename="test.jpg", colour=0, size=(1, 1))->ImageFile:
    f = BytesIO()
    image = PIL.Image.new('1', size, colour)
    image.save(f, "png")
    return ImageFile(f, name=filename)

def get_expected_image_url(file_name, request):
    return f'{request.scheme}://{request.get_host()}/media/{file_name}'