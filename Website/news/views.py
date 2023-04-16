from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from news import models
from news import forms
from news import consts as news_consts


def index(request: HttpRequest) -> HttpResponse:
    news_qs = models.News.objects.all()
    paginator = Paginator(news_qs, news_consts.PAGE_SIZE)
    page_number = request.GET.get("page") or 1
    page_news = paginator.get_page(page_number)
    context = {"news": page_news}
    return render(request, "news/index.html", context=context)


def news_create(request):
    if request.method == "POST":
        form = forms.NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("news:list")
    else:
        form = forms.NewsForm()
    return render(request, "news/create.html", context={"form": form})


def news_detail(request):
    context = {"course": models.News.objects.get(id=id)}
    return render(request, "courses/detail.html", context=context)
