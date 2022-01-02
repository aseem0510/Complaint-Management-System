from django.urls import path
from . import views


urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard"),
    # path("changePassword", views.changePassword, name="changePassword"),
    path("profile", views.profile, name="profile"),
    path("NewComplaint", views.NewComplaint, name="NewComplaint"),
]
