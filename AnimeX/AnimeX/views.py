from django.http import HttpResponse


def homePage(request):
    return HttpResponse('<h1>HOME</h1>')



def index(request):
    return render(request, 'index.html')