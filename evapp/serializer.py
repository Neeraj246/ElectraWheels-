from evapp.models import *
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model=UserTable
        fields=[ 'Name','Address','Vehiclenumber','Phone','Email']


class LoginSerializer(ModelSerializer):
    class Meta:
        model=Logintable
        fields=['username','password']        

class station_serializer(ModelSerializer):
    class Meta:
        model = StationTable
        fields = ['Name', 'latitude','longitude','Email','StationNumber']
class station_serializer1(ModelSerializer):
    class Meta:
        model = StationTable
        fields = ['id','Name', 'latitude','longitude','Email','StationNumber']


class slot_serializer(ModelSerializer):
    class Meta:
        model = SlotTable
        fields = ['Name', 'Amount','Details','Status'] 


class service_serializer(ModelSerializer):
    class Meta:
        model = ServiceTable
        fields = ['Name', 'Email','Phone','Address']               

class complaint_serializer(ModelSerializer):
    class Meta:
        model = ComplaintTable
        fields = ['Complaint','Description','Category']
class complaint_serializer1(ModelSerializer):
    class Meta:
        model = ComplaintTable
        fields = ['USER','Complaint','Description','Reply','Category']


class feedback_serializer(ModelSerializer):
    class Meta:
        model=FeedbackTable
        fields=['Feedback','Rate']      


class spare_serializer(ModelSerializer):
    class Meta:
        model=SpareTable
        fields=['id','Name','Amount','Details','image']     


class sparebooking_serializer(ModelSerializer):
    class Meta:
        model=SpareBookingTable
        fields=['USER','SPARE','Status']             
class bookinghistory_serializer(ModelSerializer):
    class Meta:
        model=SpareBookingTable
        fields=['USER','SPARE','Status']

class SlotTableserializer(ModelSerializer):
    class Meta:
        model = SlotTable
        fields = ['id','STATION', 'USER','Amount','Status']

