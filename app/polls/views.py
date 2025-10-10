from django.http import HttpResponse


def index(request):
    return HttpResponse("nice to meet you")