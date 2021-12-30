from django.urls import path
from . import views


urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard"),
    # path("changePassword", views.changePassword, name="changePassword"),
]
