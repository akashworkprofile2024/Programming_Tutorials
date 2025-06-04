from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data = {
        'title': ' Landing Page',
    }
    return render(request,'index.html',data)

def aboutus(request):
    return HttpResponse('Welcome to Django Project')

def course(request):
    return HttpResponse('Java Course')

def course_detail(request, course_id):
    return HttpResponse(course_id)

