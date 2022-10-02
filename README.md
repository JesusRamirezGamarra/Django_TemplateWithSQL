
<p align="center">
  <p align="center">    
    <img src="https://github.com/JesusRamirezGamarra/signature/blob/main/public/img/Logo_Negro.png" alt="BFFs" height="250">    
  </p>
  <p align="center">
       CoderHouse - Python
  </p>
</p>

# CH - Django with SQL
>> Consigna: Crear una web que permite ver los datos de algunos de tus familiares, guardados en un BD.

* Deberá tener un template, una vista y un modelo (como mínimo, pueden usar más)
* La clase del modelo, deberá guardar mínimo un número, una cadena y una fecha (puede guardar más cosas)
* Se deberán crear como mínimo 3 familiares
* Los familiares se deben ver desde la web.


 <p align="center">    
    <img src="https://github.com/JesusRamirezGamarra/Django_TemplateWithSQL/blob/main/public/CH-DjangoWithDB.gif" alt="django" height="450">    
  </p>


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
### Propuesta 01
```
from django.db import models
class Donation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    dateofbirht = models.DateField()
    collaboration = models.IntegerField()
    bio = models.CharField(max_length=500)
    jobrol = models.CharField(max_length=20)
    development =models.BooleanField()
    design =models.BooleanField()
    business =models.BooleanField()
``` 
### Propuesta 02
```
from django.db import models
class Donation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    dateofbirht = models.DateField()
    collaboration = models.IntegerField()
    bio = models.CharField(max_length=500)
    jobrol = models.CharField(max_length=20)
    development =models.BooleanField()
    design =models.BooleanField()
    business =models.BooleanField()

class Donation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    dateofbirht = models.DateField()
    bio = models.CharField(max_length=500)

class Collaboration(models.Model):
    collaboration = models.IntegerField()
    
class Job(models.Model):    
    # user_JobWorked = models.CharField(max_length=50)    
    jobrol = models.CharField(max_length=20)
    development =models.BooleanField()
    design =models.BooleanField()
    business =models.BooleanField()
```
### Propuesta 03
```
from django.db import models
# from datetime import date
from django.utils import timezone
from datetime import datetime

class Donation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    dateofbirht = models.DateField()
    bio = models.CharField(max_length=500)
    createdate = models.DateTimeField(auto_now_add=True)
    # createdate = models.DateTimeField(default=datetime.now())
    #createdate = models.DateField( null=True)
    #createdate = models.DateField(default=date.today())
    # createdate = models.DateField(default=django.utils.timezone.now())
    

    def __str__(self):
        return "%s %s" % (self.name,self.email)    

class Collaboration(models.Model):
    payment = models.IntegerField()
    createdate = models.DateTimeField(auto_now_add=True)
    # createdate = models.DateTimeField(default=datetime.now())
    #createdate = models.DateField( null=True)
    # createdate = models.DateField(default=date.today())
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s %s" % (self.payment,self.createdate)    
    
class Job(models.Model):    
    # user_JobWorked = models.CharField(max_length=50)    
    jobrol = models.CharField(max_length=20)
    development =models.BooleanField()
    design =models.BooleanField()
    business =models.BooleanField()
    createdate = models.DateTimeField(auto_now_add=True)
    # createdate = models.DateTimeField(default=datetime.now())
    #createdate = models.DateField( null=True)    
    # createdate = models.DateField(default=date.today())
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.jobrol        
```


* python manage.py makemigrations
  ```
  AppCoder/migrations/0001_initial.py
    - Create model Donation
  ```
* python manage.py sqlmigrate AppCoder 0001
```
BEGIN;
--
-- Create model Donation
--
CREATE TABLE "AppCoder_donation" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "email" varchar(254) NOT NULL, "dateofbirht" date NOT NULL, "collaboration" integer NOT NULL, "bio" varchar(500) NOT NULL, "jobrol" varchar(20) NOT NULL, "development" bool NOT NULL, "design" bool NOT NULL, "business" bool NOT NULL);
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

### Propuesta 01
```
from AppCoder.models import Donation
donation = Donation(
  name="Jesus Ramirez", 
  email="luciojesusramirezgamarra@gmail.com",
  dateofbirht="2000-05-14",
  collaboration=1000,
  bio="IT & Digital Manager, especialista en implementación de estrategias de transformación digital. Master in Business Administration (MBA) del AB Freeman School of Business at Tulane University ( EEUU) y de la Escuela de Negocios de la Pontificia Universidad Católica(Perú) enfocado en la gestión de proyectos ,estrategias e innovación Digital en los sectores de consumo masivo, venta directa, reparto/distribución , seguridad y gestión del riesgo . ",
  jobrol="business_owner",
  development=0,
  design=,0
  business=1
  )
curso.save()
```
### Propuesta 02
```
 Donation.objects.create(
  name="Jesus Ramirez", 
  email="luciojesusramirezgamarra@gmail.com",
  dateofbirht="2000-05-14",
  collaboration=1000,
  bio="IT & Digital Manager, especialista en implementación de estrategias de transformación digital. Master in Business Administration (MBA) del AB Freeman School of Business at Tulane University ( EEUU) y de la Escuela de Negocios de la Pontificia Universidad Católica(Perú) enfocado en la gestión de proyectos ,estrategias e innovación Digital en los sectores de consumo masivo, venta directa, reparto/distribución , seguridad y gestión del riesgo . ",
  jobrol="business_owner",
  development=0,
  design=0,
  business=1
  )

# para eliminar el registro
donation = Donation.objects.get(id=1)
donation.delete()

# para hacer un select 
#Para obtener 1 registro
donation = Donation.objects.get(id=1)
#Para obtener all registro
Lista = Donation.objects.all()
Lista.query.__str__()
'SELECT "AppCoder_donation"."id", "AppCoder_donation"."name", "AppCoder_donation"."email", "AppCoder_donation"."dateofbirht", "AppCoder_donation"."collaboration", "AppCoder_donation"."bio", "AppCoder_donation"."jobrol", "AppCoder_donation"."development", "AppCoder_donation"."design", "AppCoder_donation"."business" FROM "AppCoder_donation"'
```
### Propuesta 03
```
from AppCoder.models import Donation,Collaboration,Job

Donation.objects.create(name="Jesus Ramirez",email="luciojesusramirezgamarra@gmail.com",dateofbirht="2000-05-14", bio="IT & Digital Manager, especialista en implementación de estrategias de transformación digital. Master in Business Administration (MBA) del AB Freeman School of Business at Tulane University ( EEUU) y de la Escuela de Negocios de la Pontificia Universidad Católica(Perú) enfocado en la gestión de proyectos ,estrategias e innovación Digital en los sectores de consumo masivo, venta directa, reparto/distribución , seguridad y gestión del riesgo . ")

Collaboration.objects.create(payment=1000)

Job.objects.create(jobrol="business_owner",  development=0,  design=0,  business=1  )

donation = Donation.objects.get(id=1)
donation.1
collaboration = Collaboration.objects.get(id=1)
collaboration.payment
job = Job.objects.get(business=True)
job.jobrol

donation = Donation.objects.all()
collaboration = Collaboration.objects.all()
job = Job.objects.all()

job[0].jobrol
```

### Propuesta 04
```
python manage.py shell
from AppCoder.models import Donation,Collaboration,Job
user_email = 'luciojesusramirezgamarra@gmail.com'
donation = Donation.objects.get(email=f'{user_email}')
donation


donation = Donation.objects.filter(email=f'{user_email}12')
donation.first()
len(donation.first())


>>> donation = Donation.objects.filter(email=f'{user_email}')
>>> donation
<QuerySet [<Donation: Jesus Ramirez luciojesusramirezgamarra@gmail.com>]>
>>> len(donation)
1
>>> donation = Donation.objects.filter(email=f'{user_email}12')
>>> len(donation)
0
```

Test models :
python manage.py shell
```

from AppCoder.models import Donation,Collaboration,Job
# order by id desc
donation = Donation.objects.all().order_by('-id')
donation = Donation.objects.filter().order_by('id').reverse()
donation = Donation.objects.all().order_by('id')[::-1]



```

* python manage.py runserver

Test : 
```
python
import django
django.VERSION

```
https://zerotobyte.com/how-to-reset-the-database-in-django/

You have requested a flush of the database.
This will IRREVERSIBLY DESTROY all data currently in the "db.sqlite3" database,
and return each table to an empty state.
Are you sure you want to do this?
Type 'yes' to continue, or 'no' to cancel: yes
```