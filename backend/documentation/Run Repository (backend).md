# Run Localhost Server and Add Data
### Installations & Preparations:

- install pip and pipenv (search lng google hehe)
- add these to environment variables (path):

```powershell
[1]
C:\Users\<username>\AppData\Local\Programs\Python\Python38\Scripts\
[2] 
C:\Users\Dell\AppData\Local\Programs\Python\Python38\
```

[1] for `pip` , `pipenv` , `django-admin`

[2] for `python.exe`

- create virtual environment using pipenv
    1. cd to backend directory.
    2. do `pipenv shell`
- install project dependencies using
    ```powershell
    pipenv install
    ```
    where the pipfile & pipfile.lock files are found (backend folder)
- create database (since db is gitignored, so you have to generate one). do the ff:
    
    ```powershell
    python manage.py makemigrations
    python manage.py migrate
    ```
---
### To add data, temporarily do so in django built-in admin panel:

1. create a superuser account
    
    ```powershell
    python manage.py createsuperuser 
    ```
    
2. run server using

    ```powershell
    python manage.py runserver
    ```

1. login with new account in [`http://127.0.0.1:8000/admin/`](http://127.0.0.1:8000/admin/)