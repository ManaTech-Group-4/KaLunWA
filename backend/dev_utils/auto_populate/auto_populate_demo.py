"""
Auto-populates database for sprint review.
Prepare sample data for demo or trials on retrieving data.
Makes database deletable and buildable during complications in dev.

current generatable content:
    - superuser (user:admin, pass: admin123)
    - samples for homepage
        - dummy data
    - samples for about us
        - dummy data    
    - actual events and projects (not all are relective to actual data/lack/excess)
        - uses dummy images

requirements:
    - file names must be accurate and should be in the specified directory
         (see fields with directories e.g. images/content/...jpg)
        - will temporarily upload files to repo in its dedicated directory
            to avoid files not being found

    - as much as possible, an empty database 
        (or at least check for conflicts, then comment out object creations)

        if db is deleted, do command before running the script:

            python manage.py migrate

                - applies the actual changes on the database 
                (assuming migration files are correct, it'll go well)

            note: Migration files are a compilation of the requirements/changes
                done in the (coded) data models. 
        
            note: if deleting db raises Error: 'Resource busy', 
                try:
                    close the interactive shell in the terminal & try again.
                    close sqlite & try again.
                    stop django server & try again. 
            

to populate database, run the script ONCE:
- in cmd (backend directory), do

    python manage.py shell
            - this opens the interactive python shell. Then enter  

    exec(open("dev_utils/auto_populate/auto_populate_demo.py").read())    
"""

from django.contrib.auth import get_user_model
User = get_user_model()
#-------------------------------------------------------------------------------
# create superuser
superuser = User.objects.create_user(email='superadmin@gmail.com', password='admin123')     
superuser.is_superuser=True
superuser.is_staff=True
superuser.save()
print('populated superuser')
# create normal user
superuser = User.objects.create_user(email='admin@gmail.com', password='admin123')     
superuser.save()
print('populated normal admin user')
#-------------------------------------------------------------------------------
# homepage featured stuff
    # dummy data
exec(open("dev_utils/auto_populate/auto_populate_homepage.py").read())
print('populated for homepage featured stuff')
#-------------------------------------------------------------------------------
# about us
    # dummy data
exec(open("dev_utils/auto_populate/auto_populate_about_us.py").read())
print('populated about us stuff')
#-------------------------------------------------------------------------------
# actual camp events and projects
#     - some are still not final; see line comments
exec(open("dev_utils/auto_populate/auto_populate_camp_events_and_projects.py").read())
print('populated camp events and projects')
#-------------------------------------------------------------------------------
# actual execomm, camp leaders then dummy for commissioners and cabin officers
#     - see comments in auto_populate_org_struct file
exec(open("dev_utils/auto_populate/auto_populate_org_struct.py").read())
print('populated org struct people')
#-------------------------------------------------------------------------------
# create homepage container
exec(open("dev_utils/auto_populate/auto_populate_homepage_container.py").read())
print('created homepage container')
#-------------------------------------------------------------------------------
print('end of script')


# exec(open("dev_utils/auto_populate/auto_populate_demo.py").read())