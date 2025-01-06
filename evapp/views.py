import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate
from django.contrib import messages
from evapp.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from evapp.serializer import *

# Create your views here.

class LoginPage(View):
    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            obj=Logintable.objects.get(username=username,password=password)
            request.session['user_id']=obj.id
            if obj.type =='admin':
                return HttpResponse('''<script> alert('Login Successfully'); window.location.href='/admin_home/'; </script>''')
            # elif obj.type =='user':
            #     return render(request,'userdashboard.html')
            # else:
            #     return HttpResponse("User type not recognized")
        except Logintable.DoesNotExist:
            messages.error(request,"Invalid username or password")
            return redirect('login')
        
class Logout(View):
    def get(self, request):
        request.session.flush()
        return redirect('login')

class AdminHome(View):
    def get(self,request):
        return render(request, 'navigation.html')

# class NavigationPage(View):
#     def get(self,request):
#         return render(request, 'navigation.html')
    
class FeedbackPage(View):
    def get(self,request):
        obj= FeedbackTable.objects.all()
        return render(request, 'feedbacktable.html',{'obj':obj})
    
class AdminPage(View):
    def get(self,request):
        return render(request, 'administrator.html')    
    
class ServicePage(View):
    def get(self,request):
        obj= ServiceTable.objects.all()
        return render(request, 'manage service.html',{'obj':obj})
    
class UserPage(View):
    def get(self,request):
        obj = UserTable.objects.all()
        return render(request, 'manage user.html',{'obj':obj})   

class StationPage(View):
    def get(self,request):
        obj = StationTable.objects.all()
        return render(request, 'manage station.html',{'obj':obj})
    
class ComplaintPage(View):
    def get(self,request):
        obj = ComplaintTable.objects.all()
        return render(request, 'complainttable.html',{'obj':obj})
     
class DeleteUser(View):
    def get(self,request, id):
        obj = Logintable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script> alert('Deleted Successfully'); window.location.href='/user'; </script>''')
class AcceptStation(View):
    def get(self,request,id):
       obj=Logintable.objects.get(id=id)
       obj.type="station"
       obj.save()
       return HttpResponse('''<script> alert('Accepted Successfully'); window.location.href='/station'; </script>''')
class RejectStation(View):
    def get(self,request,id):
       obj=Logintable.objects.get(id=id)
       obj.type="reject"
       obj.save()
       return HttpResponse('''<script> alert('Rejected '); window.location.href='/station'; </script>''')    
class Acceptservicecenter(View):
    def get(self,request,id):
       obj=Logintable.objects.get(id=id)
       obj.type="service center"
       obj.save()
       return HttpResponse('''<script> alert('Accepted Successfully'); window.location.href='/service'; </script>''')
class Rejectservicecenter(View):
    def get(self,request,id):
       obj=Logintable.objects.get(id=id)
       obj.type="reject"
       obj.save()
       return HttpResponse('''<script> alert('Reject'); window.location.href='/service'; </script>''')
class Slotpage(View):
    def get(self,request):
        obj = SlotTable.objects.all()
        return render(request, 'slottable.html',{'obj':obj})
class Sparepage(View):
    def get(self,request):
        obj = SpareTable.objects.all()
        return render(request, 'sparetable.html',{'obj':obj})

class Sparebookingpage(View):
    def get(self,request):
        obj = SpareBookingTable.objects.all()
        return render(request, 'sparebookingtable.html',{'obj':obj})
    
class Deleteslot(View):
    def get(self,request, id):
        obj = SlotTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script> alert('Deleted Successfully'); window.location.href='/slot'; </script>''')    
    
class Deletespare(View):
    def get(self,request, id):
        obj = SpareTable.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script> alert('Deleted Successfully'); window.location.href='/spares'; </script>''')    


class Reply(View):
    def get(self,request, c_id):
        obj = ComplaintTable.objects.get(id=c_id)
        return render(request, 'reply.html',{'obj': obj})    
    
    def post(self,request, c_id):
        reply=request.POST['Reply']
        obj = ComplaintTable.objects.get(id=c_id)
        obj.Reply = reply
        obj.save()
        return redirect('complaint')
    

    # ///////////////////////////////////// USER API  ////////////////////////////////////
class LoginPageApi(APIView):
    def post(self, request):
        print("***********")
        response_dict = {}

        # Get data from the request
        username = request.data.get("email")
        password = request.data.get("password")
        print("username", username, password)
        # Validate input
        if not username or not password:
            response_dict["message"] = "failed"
            return Response(response_dict, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the user from LoginTable
        t_user = Logintable.objects.filter(username=username,password=password).first()

        if not t_user:
            response_dict["message"] = "failed"
            return Response(response_dict, status=status.HTTP_401_UNAUTHORIZED)

        # # Check password using check_password
        # if not check_password(password, t_user.password):
        #     response_dict["message"] = "failed"
        #     return Response(response_dict, status=HTTP_401_UNAUTHORIZED)

        # Successful login response
        response_dict["message"] = "success"
        response_dict["login_id"] = t_user.id
        response_dict["Type"] = t_user.type

        return Response(response_dict, status=status.HTTP_200_OK)

class UserReg(APIView):
    def get(self,request):
        print("######################", request.data)
        user_serial = UserSerializer(data=request.data)
        login_serial = LoginSerializer(data=request.data)
        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()

        if data_valid and login_valid:
            print("&&&&&&&&&&&&&&&&&&&&&&&&")
            password = request.data['password']
            login_profile = login_serial.save(user_type='USER', password=password)
            user_serial.save(LOGIN=login_profile)
            return Response(user_serial.data, status=status.HTTP_201_CREATED)
        return Response({'login_error': login_serial.errors if not login_valid else None,
                         'user_error': user_serial.errors if not data_valid else None}, status=status.HTTP_400)




class ViewStation(APIView):
    def get(self,request):
        station=StationTable.objects.all()
        serializer = station_serializer1(station, many = True)
        return Response(serializer.data)


    def post(self,request):
        latitude = request.data.get("lalitude")
        longitude = request.data.get("logitude")

        print("view station ----------------->", latitude, longitude)
        station=StationTable.objects.filter()
        print("station obj -----------------> ", station)
        serializer = station_serializer(station, many = True)
        return Response(serializer.data)
from geopy.distance import geodesic

def get_distance(coord1, coord2):
    """
    Calculate the distance between two coordinates using geodesic.
    coord1 and coord2 should be tuples: (latitude, longitude)
    """
    return geodesic(coord1, coord2).km 
from geopy.distance import geodesic

class NearestStationsAPI(APIView):
    def get(self, request,latitude,longitude):

        
        # User coordinates
        user_coords = (latitude, longitude)
        
        # Get all stations
        stations = StationTable.objects.all()
        nearby_stations = []

        # Loop through stations and check if they are within 5 km radius
        for station in stations:
            station_coords = (station.latitude, station.longitude)
            distance = geodesic(user_coords, station_coords).km
            if distance <= 5:
                nearby_stations.append({
                    'name': station.Name,
                    'latitude': station.latitude,
                    'longitude': station.longitude,
                    'email': station.Email,
                    'station_number': station.StationNumber,
                    'distance_km': distance,
                })

        # Return the nearby stations in the response
        return Response(nearby_stations, status=200)


        
class ViewSlot(APIView):
    def get(self,request):
        slot=SlotTable.objects.all()
        slot_serializer = slot_serializer(slot, many = True)
        return Response(slot_serializer.data) 

class ViewService(APIView):
    def get(self,request):
        print('--------------view service   ---------------->',)
        service=ServiceTable.objects.all()
        print("-----------service -->", service)
        serializer = service_serializer(service, many = True)
        return Response(serializer.data)   

class ViewSpare(APIView):
    def get(self,request):
        print('--------------view service   ---------------->',)
        spare=SpareTable.objects.all()
        print("-----------spares -->", spare)
        serializer = spare_serializer(spare, many = True)
        return Response(serializer.data)   

class ViewComplaint(APIView):
    def get(self,request,id):
        complaint=ComplaintTable.objects.filter(USER__LOGIN_id=id).all()
        complaint_ser = complaint_serializer1(complaint, many = True)
        return Response(complaint_ser.data,status=status.HTTP_200_OK) 
    
class Addcomplaint(APIView):
    def post(self,request):
        serializer=complaint_serializer(data=request.data)
        user_id=request.data.get('USER')
        user_obj=UserTable.objects.get(LOGIN_id=user_id)
        print(request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save(USER=user_obj, Reply="pending")
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class submitfeedback(APIView):
    def post(self,request):
        serializer=feedback_serializer(data=request.data)
        print("@@@@@@@@@@@@@@@@@@@@@@@@",request.data)
        user_id=request.data.get('USER')
        station_id=request.data.get('Chargingstation')
        user_obj=UserTable.objects.get(LOGIN_id=user_id)
        station_obj=StationTable.objects.get(id=station_id)
        
        print(serializer)
        if serializer.is_valid():
            serializer.save(USER=user_obj, Chargingstation=station_obj)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ViewReview(APIView):
    def get(self,request):
        complaint=FeedbackTable.objects.all()
        complaint_ser = feedback_serializer(complaint, many = True)
        return Response(complaint_ser.data) 
    
class AddReview(APIView):
    def post(self,request):
        serializer=feedback_serializer(data=request.data)
        
        print(request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    





class Addparts(View):
    def get(self, request):
        return render(request, 'Service/Addparts.html')
    

class RegSpa(View):
    def get(self, request):
        return render(request, 'Station/reg.html')
    

