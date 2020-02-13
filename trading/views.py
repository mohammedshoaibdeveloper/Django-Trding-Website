from django.shortcuts import render, HttpResponse, redirect
from trading .models import User_Signup
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session  
import requests
import json



# Create your views here.

def index(request):

    if request.session.has_key('is_loged'):
        return render(request,'home.html')

    tickerURL = "https://api.coinmarketcap.com/v1/ticker/"

        # get data from globalURL
    response = requests.get(tickerURL)
    data = response.json()
    
        
      
        # print(data)
    return render(request,'index.html',{'data':data})   

    # return render(request,'index.html')

def home(request):
    tickerURL = "https://api.coinmarketcap.com/v1/ticker/"

        # get data from globalURL
    response = requests.get(tickerURL)
    data = response.json()
        
      
        # print(data)
    return render(request,'home.html',{'data':data})   

    # return render(request,'home.html')



def signup(request):
       if request.method == 'POST':

           username = request.POST['username']
           email = request.POST['email']
           pass1 = request.POST['password']
           checkuser_name = User_Signup.objects.filter(name=username)
           checkuser_email = User_Signup.objects.filter(email=email)
           if checkuser_name:
               return HttpResponse('Username Already Exist')
           if checkuser_email:
                return HttpResponse('Email ALReady Exist')

         
           user_data = User_Signup(name=username,email=email,password = pass1)
           user_data.save()
           thank = True
           return render(request, 'index.html',{'thank':thank})
       else:
            return HttpResponse('404 error')
         
def login(request):
      if request.method == 'POST':
            username = request.POST['loginusername']
            pass1 = request.POST['loginpass']

            data = User_Signup.objects.filter(name=username,password=pass1)
            if data:
                request.session['is_loged'] = True
                tickerURL = "https://api.coinmarketcap.com/v1/ticker/"
                response = requests.get(tickerURL)
                data = response.json()
                if request.session.has_key('is_loged'):
                    return render(request,'home.html',{'data':data,'name':username})
                
            else:
                return redirect('/')    

       
    
      else:
          return redirect('/')

  





def trading(request):
    tickerURL = "https://api.coinmarketcap.com/v1/ticker/"

        # get data from globalURL
    response = requests.get(tickerURL)
    data = response.json()
        
      
        # print(data)
    return render(request,'trading.html',{'data':data})   

    #return render(requests,'trading.html')       
def wallets(request):
    return render(request,'wallets.html')
def balances(request):
    return render(request,'balances.html')
def profit(request):
    return render(request,'profit.html')
def pooling(request):
    return render(request,'pooling.html')
def trade_history(request):
    return render(request,'trade_history.html')
def edit_profile(request):
    return render(request,'edit_profile.html')
def verification(request):
    return render(request,'verification.html')
def security(request):
    return render(request,'security.html')
def account_verification(request):
    return render(request,'account_verification.html')
def logout(request):
    del request.session['is_loged']
    return redirect('/')

# def verification(request):
#      if request.method == 'POST':

#         fullname = request.POST['fullname']
#         middlename = request.POST['middlename']
#         lastname= request.POST['lastname']
#         zipcode = request.POST['zipcode']
#         city = request.POST['city']
#         region = request.POST['region']
#         conutry = request.POST['country']
#         dob = request.POST['dob']
#         passid = request.POST['passid']
#         date_of_issue = request.POST['date_of_issue']
#         expiringdatee = request.POST['expiringdate']

#         print(fullname,middlename,lastname,zipcode,city,region,conutry,dob,passid,date_of_issue,expiringdatee)

#         return render(request,'account_verification.html')
          

