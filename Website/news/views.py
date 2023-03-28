from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from news.models import News
from news import forms


def index(request: HttpRequest) -> HttpResponse:
    qs = News.objects.order_by("-created_at").all()
    return render(request, "news/index.html", {"tidings": qs})


def news_create(request):
    if request.method == "POST":
        form = forms.NewsForm(request.POST)
        if form.is_valid():
            print("Форма валидна")
            return redirect("news:list")
        else:
            return render(request, "news/create.html", context={"form": form})
    form = forms.NewsForm()
    return render(request, "news/create.html", context={"form": form})
