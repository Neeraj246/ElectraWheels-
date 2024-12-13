
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
    path('slot/',Slotpage.as_view(), name="slot"),
    path('spares/',Sparepage.as_view(), name="spares"),
    path('sparebooking/',Sparebookingpage.as_view(), name="sparebooking"),
    path('logout/',Logout.as_view(), name="logout"),
    path('complaint/',ComplaintPage.as_view(), name="complaint"),
    path('delete_user/<int:id>',DeleteUser.as_view(), name="delete_user"),
    path('accept_station/<int:id>',AcceptStation.as_view(), name="accept_station"),
    path('reject_station/<int:id>',RejectStation.as_view(), name="reject_station"),
    path('accept_service_center/<int:id>',Acceptservicecenter.as_view(), name="accept_service_center"),
    path('reject_service_center/<int:id>',Rejectservicecenter.as_view(), name="reject_service_center"),
    path('delete_slot/<int:id>',Deleteslot.as_view(), name="delete_slot"),
    path('delete_spare/<int:id>',Deletespare.as_view(), name="delete_spare"),
    path('reply/<int:c_id>',Reply.as_view(), name="reply"),
    
]
