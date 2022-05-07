import glob
import os

# deletes everything in the directory (non-recursive) that starts with 'test'
file_list = glob.glob('media/images/content/test*')
for file in file_list:
    os.remove(file)


# python manage.py shell
# exec(open("dev_utils/delete_test_files.py").read())

