from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

app_name="customersurvey"

urlpatterns = [
    # path("", views.index, name="index"),
    path('survey/',views.survey, name='survey'),
    path('save/question/',views.save_question, name='save_question'),
    # path('sur/',views.sur, name='sur'),
]
