from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

def insert_topic(request):
    tn=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('topic name inserted successfully')

def insert_Webpage(request):
    tn=input('enter topic_name : ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter name : ')
    u=input('enter url : ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('name inserted successfully')

def insert_AccessRecords(request):
    tn=input('enter topic_name: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0] 
    TO.save()
    n=input('enter name : ')
    u=input('enter url : ') 
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    a=input('enter author')
    d=input('enter date')
    AccessRecordObjects=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    AccessRecordObjects.save()
    return HttpResponse('author inserted successfully')


