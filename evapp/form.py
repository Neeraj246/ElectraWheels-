from django.forms import ModelForm

from evapp.models import *


class StationRegForm(ModelForm):
    class Meta:
        model=StationTable
        fields = ['Name', 'latitude', 'longitude', 'Email', 'StationNumber']

class ServiceRegForm(ModelForm):
    class Meta:
        model=ServiceTable
        fields=['Name','Email','Phone','Address']


class AddpartsForm(ModelForm):
    class Meta:
        model=SpareTable
        fields=['image','Name','Amount','Details','SERVICE']
class EditpartsForms(ModelForm):
    class Meta:
        model=SpareTable
        fields=['image','Name','Amount','Details']

class Alert_Form(ModelForm):
    class Meta:
        model = Alert
        fields = ['Alert']