from datetime import datetime
from django.utils.text import slugify

def to_formal_mdy(date:datetime)->str:
        if not date:
            return None
        return f'{date.strftime("%B")} {date.day}, {date.year}' 

def get_value_by_label(label:str, Enum): 
	if not label in Enum.labels:
		return None

	for enum_obj in Enum.__members__.values(): # enum members -> key:name, value:enum_obj { 'PRESIDENT': OrgLeader.Positions.PRESIDENT }
		if label == enum_obj.label: 
			value = enum_obj.value
	return value

def unique_slugify(instance, string):
	model = instance.__class__
	slug = slugify(string)
	unique_slug = slug
	suffix = 1
	while model.objects.filter(slug=unique_slug).exists():
		unique_slug = f'{slug}-{suffix}'
		suffix += 1
	return unique_slug 