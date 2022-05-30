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
	
	# ensure that when doing a put request, or updating an entry in the database,
	# it does not change the slug of the object
	# why does the slug change? this is because the presave signal triggers the
		# updating of the slug value, to which a search is done to see if an existing
		# slug had been used. The problem is, when a record is saved due to an update, 
		# it retriggers the signal to generate a slug value from the name, and when this
		# name is not changed during an update, the slug generated from it is compared
		# to the old record, which is still the same name. It detects it as a duplicate, 
		# and rewrites the slug by appending the corresponding suffix.

	while True:
		db_instance_list = model.objects.filter(slug=unique_slug)

		if not db_instance_list: # empty
		# if it's empty then the slug is unique
			return unique_slug

		if len(db_instance_list) == 1 and db_instance_list[0].id == instance.id:
		# check to avoid rewriting its own slug 
			return unique_slug
		else:
			unique_slug = f'{slug}-{suffix}'
			suffix += 1
		