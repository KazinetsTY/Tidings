from django.http import HttpResponse, HttpRequest

from news.models import News
from django.template import loader


def index(request: HttpRequest) -> HttpResponse:
    template = loader.get_template('news/index.html')
    qs = News.objects.order_by("-created_at").all()
    context = {"tidings": qs}
    return HttpResponse(template.render(context, request))
