from django.urls import path 
from .views import * 

urlpatterns = [
    path('about', AboutView.as_view()),

    path('work', WorkView.as_view())
]