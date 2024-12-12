import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate
from django.contrib import messages
from evapp.models import *
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



