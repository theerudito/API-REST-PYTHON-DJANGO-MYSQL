API REST DJANGO MYSQL


STEP 1.- create a new environment in Python (virtualenv) example python3 -m venv tutorial-env

STEP 2.- install django

STEP 3.- create a project with command python django-admin startproject mysite

STEP 4.- create a new folder with command python manage.py startapp app 

STEP 5.- configure the proyect in settings.py

STEP 6.- in INSTALLED_APPS add app

STEP 7.- configure the database in settings.py  in DATABASES

STEP 8.- in file models.py create a model

STEP 9.- in file panel admin admin.py register your model Example Company

STEP 10.- inside the mysite execute command python manage.py migrate

STEP 11.- create a superuser in admin panel execute command python manage.py createsuperuser

STEP 12.- migrate the model execute command python manage.py makemigrations

STEP 13.- migrate the model execute command python manage.py migrate

STEP 14.- execute the project execute command python manage.py runserver

STEP 14.- execute the project execute command python manage.py runserver

STEP 15.- create a new file inside the app folder with the name urls.py

STEP 16.- import the view Example CompanyViews

STEP 17.- register the view in urls.py the project name is mysite 

STEP 18.- in the file views.py import the model Example Company

STEP 19.- with postman or another app you can using the url http://127.0.0.1:8000/app/companies/

STEP 20.- using all the methods example get, post, put, delete

STEP 21.- good luck

file document using command pip install -r requirements.txt
