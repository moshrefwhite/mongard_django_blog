from django.http import HttpResponse

def say_hello(request):
    return HttpResponse('hello')



