
from django.contrib import admin
from django.urls import path

from evapp.views import *

urlpatterns = [
    path('', LoginPage.as_view(), name="login"),
    path('admin_home/',AdminHome.as_view(), name="admin_home"),
    # path('navigation/',NavigationPage.as_view(), name="navigation"),
    path('feedback/',FeedbackPage.as_view(), name="feedback"), 
    path('adminpage/',AdminPage.as_view(), name="administrator"),
    path('service/',ServicePage.as_view(), name="service"),
    path('user/',UserPage.as_view(), name="user"),
    path('station/',StationPage.as_view(), name="station"),
    path('logout/',Logout.as_view(), name="logout"),
    path('complaint/',ComplaintPage.as_view(), name="complaint"),
    path('delete_user/<int:id>',DeleteUser.as_view(), name="delete_user"),
]
