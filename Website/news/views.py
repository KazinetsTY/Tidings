from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Новости<h1>")
