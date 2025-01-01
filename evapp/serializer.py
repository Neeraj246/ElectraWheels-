from evapp.models import *
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model=UserTable
        fields=['LOGINID', 'name','place','age','phone','email']


class LoginSerializer(ModelSerializer):
    class Meta:
        models=Logintable
        fields=['username','password']        

class station_serializer(ModelSerializer):
    class Meta:
        model = StationTable
        fields = ['image', 'station_id']


class slot_serializer(ModelSerializer):
    class Meta:
        model = SlotTable
        fields = ['image', 'slot_id'] 


class service_serializer(ModelSerializer):
    class Meta:
        model = ServiceTable
        fields = ['image', 'service_id']               


class complaint_serializer(ModelSerializer):
    class Meta:
        model = ComplaintTable
        fields = ['image', 'complaint_id']
