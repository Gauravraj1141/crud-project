from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.registeration, name="registeration"),
    path("update/<int:upid>/", views.updates, name="updates"),
    path("delete/<int:user>/", views.delete, name="delete"),
]
