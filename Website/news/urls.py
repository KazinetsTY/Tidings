from django.urls import path
from news import views

app_name = "news"

urlpatterns = [
    path("", views.index, name="list"),
    path("create/", views.news_create, name="create"),
#    path("<int:id/>", views.news_detail, name="detail"),
]
