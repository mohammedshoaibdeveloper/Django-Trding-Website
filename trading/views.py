from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from trading .models import User_Signup , Verification ,statuses ,transictions
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session  
from django.contrib import messages
from django.http import HttpResponse
import requests
import json
import stripe


# Create your views here.
stripe.api_key='sk_test_ORxhe7Gpc4OeUzSfyeqkGwES00S8EeM2v0'
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

def homee(request):
    tickerURL = "https://api.coinmarketcap.com/v1/ticker/"

        # get data from globalURL
    response = requests.get(tickerURL)
    data = response.json()
        
      
        # print(data)
    return render(request,'home.html',{'data':data,'uid':request.session['id']})   

    # return render(request,'home.html')



def signup(request):
       if request.method == 'POST':

           username = request.POST['username']
           email = request.POST['email']
           pass1 = request.POST['password']
           checkuser_name = User_Signup.objects.filter(name=username)
           checkuser_email = User_Signup.objects.filter(email=email)
           if checkuser_name or checkuser_email:
                messages.info(request,"The user is already signup")
                return redirect('/')
            
           if len(username) > 30 or len(username) < 3:
                return HttpResponse("Username not grater than 30 and not less then 3")
           if not username.isalnum():
                return HttpResponse("Username should contain only letters and numbers")
               
           

         
           user_data = User_Signup(name=username,email=email,password = pass1)
           user_data.save()
           thank = True
           return render(request, 'index.html',{'thank':thank})
       else:
            return HttpResponse('404 error')
         
def login(request):
      if request.method == 'POST':
            userid=0
            upadateId=0
            username = request.POST['loginusername']
            pass1 = request.POST['loginpass']
           

            data = User_Signup.objects.filter(name=username,password=pass1)
           

            if data:
                request.session['is_loged'] = True
                y=User_Signup.objects.raw(f'select * FROM trading_User_Signup where name="{username}"')
                for x in y:
                    userid=x.name
                    upadateId=x.sno
                request.session['id'] = userid
               
                tickerURL = "https://api.coinmarketcap.com/v1/ticker/"
                response = requests.get(tickerURL)
                data = response.json()
                if request.session.has_key('is_loged'):
                    return render(request,'home.html',{'data':data,'uid':request.session['id']})
                
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
    return render(request,'trading.html',{'data':data,'uid':request.session['id']})   

    #return render(requests,'trading.html')       
def wallets(request):
    return render(request,'wallets.html',{'uid':request.session['id']})
def balances(request):
    return render(request,'balances.html',{'uid':request.session['id']})
def profit(request):
    return render(request,'profit.html',{'uid':request.session['id']})
def pooling(request):
    return render(request,'pooling.html',{'uid':request.session['id']})
def trade_history(request):
    return render(request,'trade_history.html',{'uid':request.session['id']})
def edit_profile(request):
     datalist=request.session['id'] 
   
     if request.method=="POST":
         update = User_Signup.objects.get(name=datalist)
         update.email= request.POST['email']
         update.password= request.POST['changepassword']
         update.profileimg= request.FILES['image']
         update.save()
     edit=User_Signup.objects.raw(f'select * FROM trading_User_Signup where name="{datalist}"')
        
     return render(request,'edit_profile.html',{"data":edit,'uid':request.session['id']})
def verification(request):
    return render(request,'verification.html',{'uid':request.session['id']})
def security(request):
    return render(request,'security.html',{'uid':request.session['id']})
def account_verification(request):
    datalist=request.session['id']
    if request.method == 'POST':
        name= request.POST['username']
        fullname = request.POST['fullname']
        middlename = request.POST['middlename']
        lastname= request.POST['lastname']
        zipcode = request.POST['zipcode']
        city = request.POST['city']
        region = request.POST['region']
        country = request.POST['country']
        dob = request.POST['dob']
        passid = request.POST['passid']
        date_of_issue = request.POST['date_of_issue']
        expiringdatee = request.POST['expiringdate']
        address1= request.POST['address1']
        address2= request.POST['address2']
        passportimg= request.FILES['passportimg']
        selfieimg= request.FILES['selfieimg']
        idbackimg= request.FILES['idbackimg']
        documentwithaddimg= request.FILES['documentwithaddimg']
        
        user_data =Verification(uname=name,fullname=fullname,middlename=middlename,lastname=lastname,address1=address1,
        address2=address2,zipcode=zipcode,city=city,region=region,country=country,dob=dob,passid=passid,
        date_of_issue=date_of_issue,expiringdate=expiringdatee,passportimg=passportimg,idbackimg=idbackimg,documentwithaddimg=documentwithaddimg)
        checkuser_user = Verification.objects.filter(uname=name)
        if checkuser_user:
            messages.info(request,"The user is already verified")
            return redirect('account_verification')
   
        
        user_data.save()
        #return render(request,'home.html')
    
    edit=Verification.objects.raw(f'select * FROM trading_Verification where uname="{datalist}"')
    if not edit:
        status = False
    else:
        status = True    
    #edit = Verification.objects.get(uname=datalist)

 


    
    return render(request,'account_verification.html',{"data":edit,"status":status,"uid":request.session['id']})
def logout(request):
    del request.session['is_loged']
    del request.session['id']
   
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
          


def home(request):
    return render(request,'home.html',{'uid':request.session['id']})

def charge(request):
    if request.method == 'POST':
        x=int(request.POST['amount'])
           
        charge = stripe.Charge.create(
        amount=x*100,
        currency='usd',
        description='A Django charge',
        source=request.POST['stripeToken']
        )
#         tuser_id
# tamout
# token
# status_id
        # return render(request,'charge.html')
        if(charge['paid']==True):
            payment = transictions(tuser_id=request.session['id'],tprice=x,tamout=222,token=request.POST['stripeToken'],status_id_id=0)
            payment.save()

            return HttpResponse('source')