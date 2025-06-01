from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,'index.html')

def course(request):
    return HttpResponse(' Java Course ')

def coursedetails(request, courseid):
    return HttpResponse(courseid)

