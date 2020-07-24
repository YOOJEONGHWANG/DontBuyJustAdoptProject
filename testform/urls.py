from testform import views
from django.urls import path

urlpatterns=[
    path("form/", views.form),
    path("response/", views.response)
]