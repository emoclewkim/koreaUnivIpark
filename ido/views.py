from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Survey
from django.utils import timezone

# Create your views here.

def home(request):
    return render(request, 'home.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    survey = Survey()

    survey.name = request.GET['name']
    survey.major = request.GET['major']
    survey.phone_num = request.GET['phone_num']
    survey.body_temp = request.GET['body_temp']
    survey.agree_check = request.GET['chk_info']
    survey.update_time = timezone.datetime.now()

    survey.save()
    return HttpResponseRedirect(reverse('new'))