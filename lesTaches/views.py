from django.http import HttpResponse

def home(request, name):
    return HttpResponse("<h1>Bonjour </h1>"+name)