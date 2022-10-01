from pipes import Template
from django.http import HttpResponse
# from django.views import View
import random
import datetime

import os
from django.template import Template,Context


from django.conf import settings
# from django.conf.urls.static import static

from django.shortcuts import render
#from AppCoder.models import Profesor

from django.template import loader


def init(request):
    template = loader.get_template("template_desafio.html")
    
    diccionario = {"author":settings.AUTHOR}
    res = template.render(diccionario)
    return HttpResponse(res)    

def sendEmail(request, *args, **kwargs):
    print("request : ",request)
    request.resolver_match.kwargs.get('url_param')

    template = loader.get_template("template_desafio.html")    
    diccionario = {"author":settings.AUTHOR}
    res = template.render(diccionario)
    return HttpResponse(res)      
