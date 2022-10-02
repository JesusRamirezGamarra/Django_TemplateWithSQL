from pipes import Template
from django.http import HttpResponse
# from django.views import View
# import random
# import datetime

# import os
# from django.template import Template,Context


from django.conf import settings
# from django.conf.urls.static import static

from django.shortcuts import render

from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum

from AppCoder.models import Donation,Collaboration,Job

from datetime import date

def init(request):
    

    result = Collaboration.objects.values('donation').order_by('donation').annotate(total_price=Sum('payment'))        
    print(result)


    template = loader.get_template("template_desafio.html")
    
    diccionario = {"author":settings.AUTHOR}
    res = template.render(diccionario)
    return HttpResponse(res)    

@csrf_exempt
def send_donation(request):
    
    print(request.POST)
    # diccionario = {}
    # template = loader.get_template("template_desafio.html")
    if request.method == "POST":
        user_name = request.POST["user_name"]
        user_email = request.POST["user_email"]
        user_dateofbirht = request.POST["user_dateofbirht"]
        user_bio = request.POST["user_bio"]
        print('user_name',user_name)
        print('user_email',user_email)
        print('user_dateofbirht',user_dateofbirht)
        print('user_bio',user_bio)
                
        user_collaboration = request.POST["user_collaboration"]
        print('user_collaboration',user_collaboration)
                
        user_job = request.POST["user_job"]
        user_development =False
        user_design =False
        user_business =False
    
        print('user_job',user_job)        


        interests =  request.POST["interests"]
        for item in interests:
            if item == 'user_development':
                user_development = True
            if item == 'user_design':
                user_design = True
            if item == 'user_business':
                user_business = True                

        print('user_development',user_development)
        print('user_design',user_design)
        print('user_business',user_business)
        
        
        # Donation.objects.create(    
        #     name= user_name,
        #     email=user_email,
        #     dateofbirht=user_dateofbirht,
        #     bio=user_bio 
        # )
        
        # Collaboration.objects.create(
        #     payment= user_collaboration
        # )
        
        # Job.objects.create(
        #     jobrol= user_job,
        #     development= user_development,  
        #     design= user_design,  
        #     business= user_business 
        # )
        
        donation = Donation.objects.filter(email=f'{user_email}')
        if len(donation) == 0:
            donation = Donation(
                name= user_name,
                email=user_email,
                dateofbirht=user_dateofbirht,
                bio=user_bio,
                createdate = date.today() 
                )
            donation.save()
        else:
            donation = donation.first()
        
        collaboration = Collaboration(
            payment= user_collaboration,
            createdate = date.today(),
            donation=donation
        )
        collaboration.save()
        
        job = Job(
            jobrol= user_job,
            development= user_development,  
            design= user_design,  
            business= user_business,
            createdate = date.today(),
            donation=donation            
        )
        job.save()
        
        
        
        donation = Donation.objects.all().order_by('-id')
        collaboration = Collaboration.objects.all()
        job = Job.objects.all()
        
        # print(collaboration)

        diccionario = {
            "donation":donation, 
            "collaboration":collaboration,
            "job":job
            }
        template = loader.get_template("gracias.html")
            
    res =  template.render(diccionario)
    return HttpResponse(res)  