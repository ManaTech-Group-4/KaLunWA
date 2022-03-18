# from kalunwa.content.models import Announcement, Event


# q1 = Announcement.objects.order_by('-created_at') # latest
# q1_creation = q1[0].created_at


# featured_events = Event.objects.filter(is_featured=True)[:3]

# plain_events = Event.objects.filter(is_featured=False)

# print(f'featured: {featured_events}')
# print(f'plain: {plain_events}')
#passed_courses = Course.objects.filter(course_attempts__student=1, course_attempts__academic_status=CourseAttempt.AcademicStatusChoice.PASSED)
#program_required_courses = Course.objects.filter(programs__id=16)



#exec(open("kalunwa/content/query_practice.py").read())

#==============================================================================

