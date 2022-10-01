

https://learn.microsoft.com/en-us/windows/python/web-frameworks
* python3 -m venv .venv
* source .venv/bin/activate
* pip install Django
* python3 -m pip install --upgrade pip
* django-admin startproject web_project
* cd web_project
* python manage.py migrate
* python manage.py runserver

* python manage.py startapp AppCoder
* python manage.py migrate
```
Create Directorys
  Create statics
  Create templates

Add Aplications in settings.py of web_project
  INSTALLED_APPS = [
      "django.contrib.admin",
      "django.contrib.auth",
      "django.contrib.contenttypes",
      "django.contrib.sessions",
      "django.contrib.messages",
      "django.contrib.staticfiles",
      "AppCoder"
  ]

Create Const STATICFILES_DIRS in settings.py of web_project

STATICFILES_DIRS = [
    #BASE_DIR  /"statics"
    os.path.join(BASE_DIR, 'statics'),
]


```
* python manage.py check AppCoder
  ```
  System check identified no issues (0 silenced).
  ```
En models.py agregamos : 
```
from django.db import models

class Curso(models.Model):
    
    nombre=models.CharField(max_length=40)
    camada=models.SmallIntegerField()
    
class Estudiante(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()

class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    profesor=models.CharField(max_length=30)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaEntrega = models.DateField()
    entregado =models.BooleanField()
``` 

* python manage.py makemigrations
  ```
  Migrations for 'AppCoder':
  AppCoder/migrations/0001_initial.py
    - Create model Curso
    - Create model Entregable
    - Create model Estudiante
    - Create model Profesor
  ```
* python manage.py sqlmigrate AppCoder 0001
```
BEGIN;
--
-- Create model Curso
--
CREATE TABLE "AppCoder_curso" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(40) NOT NULL, "camada" smallint NOT NULL);
--
-- Create model Entregable
--
CREATE TABLE "AppCoder_entregable" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(30) NOT NULL, "fechaEntrega" date NOT NULL, "entregado" bool NOT NULL);
--
-- Create model Estudiante
--
CREATE TABLE "AppCoder_estudiante" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(30) NOT NULL, "apellido" varchar(30) NOT NULL, "email" varchar(254) NOT NULL);
--
-- Create model Profesor
--
CREATE TABLE "AppCoder_profesor" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(30) NOT NULL, "apellido" varchar(30) NOT NULL, "email" varchar(254) NOT NULL, "profesor" varchar(30) NOT NULL);
COMMIT;
```
* python manage.py migrate
```
Operations to perform:
  Apply all migrations: AppCoder, admin, auth, contenttypes, sessions
Running migrations:
  Applying AppCoder.0001_initial... OK
```
* python manage.py shell
```
from AppCoder.models import Curso
curso = Curso(nombre="Python", camada=23800)
curso.save()
```

* python manage.py runserver

Test : 
```
python
import django
django.VERSION
```