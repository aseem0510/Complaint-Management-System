from django.urls import path
from . import views


urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard"),
    # path("changePassword", views.changePassword, name="changePassword"),
    path("profile", views.profile, name="profile"),
    path("NewComplaint", views.NewComplaint, name="NewComplaint"),
    path("ComplaintHistory", views.ComplaintHistory, name="ComplaintHistory"),
    path("render_pdf_view", views.render_pdf_view, name="render_pdf_view")
]
