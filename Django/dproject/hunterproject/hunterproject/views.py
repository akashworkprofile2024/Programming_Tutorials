from django.http import HttpResponse

def aboutus(request):
    return HttpResponse('<b>Welcome to the About Us page of the Hunter Project!</b>')

def course(request):
    return HttpResponse(' Java Course ')

def coursedetails(request, courseid):
    return HttpResponse(courseid)