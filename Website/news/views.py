from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from news import models
from news import forms


def index(request: HttpRequest) -> HttpResponse:
    qs = models.News.objects.order_by("-created_at").all()
    return render(request, "news/index.html", {"tidings": qs})


def news_create(request):
    if request.method == "POST":
        form = forms.NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("news:list")
    else:
        form = forms.NewsForm()
    return render(request, "news/create.html", context={"form": form})
