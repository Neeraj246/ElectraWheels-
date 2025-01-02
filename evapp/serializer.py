from evapp.models import *
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model=UserTable
        fields=[ 'Name','Address','Vehiclenumber','Phone','Email']


class LoginSerializer(ModelSerializer):
    class Meta:
        models=Logintable
        fields=['username','password']        

class station_serializer(ModelSerializer):
    class Meta:
        model = StationTable
        fields = ['Name', 'latitude','longitude','Email','StationNumber']


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
        fields = ['Complaint', 'Date','Reply']


class feedback_serializer(ModelSerializer):
    class Meta:
        model=FeedbackTable
        fields=['Feedback','Date','Review']      


class spare_serializer(ModelSerializer):
    class Meta:
        model=SpareTable
        fields=['Name','Amount','Details']     


class sparebooking_serializer(ModelSerializer):
    class Meta:
        model=SpareBookingTable
        fields=['SpareName','Amount','Quantity','Status']             

