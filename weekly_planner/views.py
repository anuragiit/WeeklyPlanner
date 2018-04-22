# noinspection PyUnresolvedReferences
from django.shortcuts import render,redirect
# noinspection PyUnresolvedReferences
from django.http import HttpResponse,HttpResponseRedirect
# noinspection PyUnresolvedReferences
from django.contrib.auth.models import User
# noinspection PyUnresolvedReferences
from django.contrib.auth import authenticate,login
# noinspection PyUnresolvedReferences
from django.contrib.auth.decorators import login_required
from .models import toDoList
from django.core import serializers
import json


def homepage(request):
    if request.method == "POST" and 'taskName' in request.POST:
        taskName=request.POST['taskName']
        description=request.POST['description']
        newEnty = toDoList(userdetails= request.user, taskName = taskName, description = description, status = "TODO")
        newEnty.save()
        return HttpResponseRedirect('/home/profile') 
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/profile')
    if request.method == "POST" and 'form-user-name' in request.POST:
        username_form= request.POST['form-user-name']
        first_form=request.POST['form-first-name']
        Last_form = request.POST['form-last-name']
        Email_form = request.POST['form-email']
        Pass_form = request.POST['form-pass-word']
        user = User.objects.create_user(username=username_form, password=Pass_form,email=Email_form,first_name=first_form,last_name=Last_form)
        login(request, user)
        return HttpResponseRedirect('/home/profile') 

    if request.method == "POST" and 'form-username' in request.POST:
        username_login=request.POST['form-username']
        password_login=request.POST['form-password']
        user = authenticate(username=username_login, password=password_login)
        if user:
            login(request, user)
            return HttpResponseRedirect('/home/profile')
        else:
             return render(request,'homepage.html',{"msg":"login failed"})
    

        
    return render(request,'homepage.html')

@login_required
def userprofile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
        
    tasks= toDoList.objects.filter(userdetails = request.user,status__in=["COMPLETED","TODO","INPROGRESS"])
    completed = toDoList.objects.filter(userdetails = request.user,status="COMPLETED")
    todo = toDoList.objects.filter(userdetails = request.user,status="TODO")
    inprogress = toDoList.objects.filter(userdetails = request.user,status="INPROGRESS")
    return render(request,'cards.html',{"tasks":tasks,"completed":completed, "todo":todo, "inprogress": inprogress})



def taskstatus(request,offset):
    newtype = offset.split("-")[0]
    taskid =  offset.split("-")[1]
    newstatus = toDoList.objects.get(id = taskid)
    newstatus.status = newtype
    newstatus.save()
    return HttpResponseRedirect('/home/profile')











