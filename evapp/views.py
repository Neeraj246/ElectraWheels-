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
        station_serializer = station_serializer(station, many = True)
        return Response(station_serializer.data)
        
class ViewSlot(APIView):
    def get(self,request):
        slot=SlotTable.objects.all()
        slot_serializer = slot_serializer(slot, many = True)
        return Response(slot_serializer.data) 

class ViewService(APIView):
    def get(self,request):
        service=ServiceTable.objects.all()
        service_serializer = service_serializer(service, many = True)
        return Response(service_serializer.data)   

class ViewComplaint(APIView):
    def get(self,request):
        complaint=ComplaintTable.objects.all()
        complaint_serializer = complaint_serializer(complaint, many = True)
        return Response(complaint_serializer.data) 




