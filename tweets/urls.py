from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweets ,name='tweets'),
    path('search-hashtag/', views.searchHashtags ,name='search-hashtag'),
]
