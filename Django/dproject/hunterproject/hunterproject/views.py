from django.http import HttpResponse

def aboutus(request):
    return HttpResponse('Welcome to the About Us page of the Hunter Project!')