from django.urls import path

from . import views

urlpatterns = [
    path("",views.reskill_data, name = "data")
]



