
from django.contrib import admin
from django.urls import path

from evapp.views import *

urlpatterns = [
    path('login', LoginPage.as_view(), name="login"),
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
    path('stationviewreview',stationviewreview.as_view(),name='stationviewreview'),
    


# /////////////////////////////////// API ////////////////////////////////////

    path('LoginPageApi',LoginPageApi.as_view(), name='LoginPageApi'),
    path('viewStations',ViewStation.as_view(), name='viewStations'),
    path('submitfeedback',submitfeedback.as_view(), name='submitfeedback'),
    path('ViewService',ViewService.as_view(), name='ViewService'),
    path('bookstationslot',bookstationslot.as_view(),name='bookstationslot'),
    path('bookstationslothistory/<int:id>',bookstationslothistory.as_view(),name='bookstationslothistory'),

    path('ViewSpare',ViewSpare.as_view(), name='ViewSpare'),
    path('Bookspare',Bookspare.as_view(),name='Bookspare'),
    path('Viewbookinghistory/<int:id>',Viewbookinghistory.as_view(),name='Viewbookinghistory'),
    path('ViewComplaint/<int:id>',ViewComplaint.as_view(),name='ViewComplaint'),
    path('Addcomplaint',Addcomplaint.as_view(),name='Addcomplaint'),
    path('ViewReview',ViewReview.as_view(),name='ViewReview'),
    path('AddReview',AddReview.as_view(),name='AddReview'),
    path('NearestStationsAPI/<int:latitude>/<int:longitude>',NearestStationsAPI.as_view(),name='NearestStationsAPI'),


    


    #////////////////////////////station///////////////


path('reg',Reg.as_view(), name='reg'),
path('',Index.as_view()),
path('dash',Dash.as_view(),name='dash'),
path('viewstations',ViewStations.as_view(),name='viewstations'), 
path('managebooking',ManageBooking.as_view(),name='managebooking'),
path('viewreview',ViewReview.as_view(),name='viewreview'),
path('base',Base.as_view(),name='base'),
path('alert',Emergencyalert.as_view(),name='alert'),
path('alertsend', AlertSend.as_view(), name='alertsend'),
path('viewalert', ViewAlert.as_view(), name='viewalert'),



##########################################service#################################

path('addparts', Addparts.as_view(), name='addparts'),
path('regspa', RegSpa.as_view(), name='regspa'),
path('servreg',Servreg.as_view(), name='servreg'),
path('serviceDas',ServiceDas.as_view(),name='serviceDas'),
path('vieworders',Vieworders.as_view(),name='vieworders'),
path('manparts',ManParts.as_view(),name='manparts'),
path('baseserv',BaseServ.as_view(),name='baseserv'),
path('deleteprt/<int:pk>/',Deleteparts.as_view(),name='deleteprt'),
path('edit/<int:pk>/',Editparts.as_view(),name='edit'),
path('acceptorder/<int:id>',AcceptOrder.as_view(), name="acceptorder"),
path('rejectorder/<int:id>',RejectOrder.as_view(), name="rejectorder"),
path('acceptslot/<int:id>',AcceptSlot.as_view(), name="acceptslot"),
path('rejectslot/<int:id>',RejectSlot.as_view(), name="rejectslot"),
]