from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
# from .models import *
from .serializers import RegisterSerializer
from django.contrib.auth.hashers import make_password
from django.contrib import auth
import datetime
from datetime import timedelta
from datetime import datetime as dt



import random
import string
import requests
import json
from django.http import HttpResponseRedirect
from .payment import init_payment
import math

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# from .forms import UserRegisterForm
from .models import *
from django.contrib.auth.models import User
from django.core.mail import send_mail
# from .utilis import refcode
import uuid

from funmize import settings



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt





# Create your views here.
def index(request):
    return render (request, 'funmizesub/index.html' )

def reg(request):
    return render (request, 'funmizesub/reg.html')

def signin(request):
	return render(request, 'login.html')


def check_mail_ajax(request):
	if request.is_ajax():
		email = request.GET.get('email', None)
		check_email = User.objects.filter(email=email).exists()
		if check_email == True:
			response = {'error': 'Email already exists.'}
			return JsonResponse(response)
		else:
			response = {'success': 'Cool'}
			return JsonResponse(response)
	else:
		response = {'error': 'Error Email Checking.'}
		return JsonResponse(response)


class Register(APIView):
	def post(self, request):
		serializer = RegisterSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			obj = serializer.save()
			password = make_password(serializer.data['password'])
			User.objects.filter(email=serializer.data['email']).update(password=password)
			get_membership = Membership.objects.get(membership_type='Free')
			instance = UserMembership.objects.create(user=obj, membership=get_membership)
			return Response({'success': 'Registration successful.'})
		else:
			return Response({'error': 'Error. Try again'})


class Login(APIView):
	def post(self, request):
		email = request.data.get('email')
		password = request.data.get('password')

		# Let us check if the user exists or not...
		check_email = User.objects.filter(email=email).exists()
		if check_email == False:
			return Response({'error': 'No account with such email'})
		# We need to check if the user password is correct
		user = User.objects.get(email=email)
		if user.check_password(password) == False:
			return Response({'error': 'Password is not correct. Try again'})
		# Now let us log the user in
		log_user = auth.authenticate(email=email, password=password)
		if user is not None:
			auth.login(request, log_user)
			return Response({'success': 'Login successful'})
		else:
			return Response({'error': 'Invalid email/password. Try again later.'})





















































@csrf_exempt
def contact (request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        contactinfo = Contactinfo(name=name,email=email,phone=phone,subject=subject,message=message)
        contactinfo.save()
        messages.success(request,'Your message has been sent successfully, we will get back to you soon!')
        return redirect ('contact')
    else:
        print('am gettin bored')
    return render (request, 'funmizesub/contact.html' )


# @login_required
def dashboard(request):
    name = request.user.id
    # print(name)
    allhistory = Transhistory.objects.filter(user=name)
    # userwallet = UserWallet.objects.get(user=request.user)
    # print(userwallet)

    context = {
        'history':allhistory,
        # 'userwallet':userwallet
    }
    return render(request, 'funmizesub/dashboard.html', context)


# 
# @csrf_exempt
# def register(request):
    # if request.method == 'POST':
    #    form = UserRegisterForm(request.POST)
    #    if form.is_valid():
            # form.save()
# 
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username,password=password)
# 
            # added this for error message
            # if user :
                # login(request,user)
                # return redirect('dashboard')
            # else :
                # messages.error(request,'There is something wrong with your input, please check through and get back to us!')
                # return redirect ('register')
    #    else:
            # print('Form not valid')
            # messages.error(request,'There is something wrong with your input, please check through and get back to us!')
            # return redirect ('register')
# 
    # else:
        # form = UserRegisterForm()
    # context = {
    #    'form':form
    # }
    # return render (request, 'registration/register.html', context)


@login_required
def addtouser(request):
    if request.method =='POST':
        email = request.POST['atuemail']
        amount = request.POST['atuamount']
    
        addbalancetouser = Addbalancetouser(email=email,amount_to_add=amount)
        addbalancetouser.save()

        if email == request.user.email:
            print(email + ' You have been funded = ' + amount)
            return redirect ('dashboard')

    else:
        print('Why are u not working ')
    return render (request, 'funmizesub/addtouser.html' )


def funding(request):
    return render (request, 'funmizesub/funding.html' )

@csrf_exempt
def fundings(request):
    if request.method == 'POST':
        email = request.POST['email']
        amount = request.POST['payamount']
        firstname = request.user.first_name
        lastname = request.user.last_name
        amount = int(amount)*100
        # print(email)print(firstname)print(lastname)print(amount)
        initialized = init_payment(firstname, lastname, email, amount)
        # print('walaaaaaaaaaaaaaaaaaaas4')
        print(initialized["data"]["authorization_url"])
        amount = amount/100
        instance = PayHistory.objects.create(amount=amount, payment_for='wallet funding', user=request.user, paystack_charge_id=initialized['data']['reference'], paystack_access_code=initialized['data']['access_code'])
        
        # wallet = UserWallet.objects.get(user=request.user)
        # old_amt = wallet + amount
        # wallet.save()
        
        # prevbal = UserWallet.objects.get(user=request.user)
        # prevbal = int(prevbal.amount)
        # print(prevbal)
        # newbal = prevbal + amount
        # UserWallet.objects.update(amount=newbal)
        link = initialized['data']['authorization_url']
        return HttpResponseRedirect(link)
    return render (request, 'funmizesub/fundings.html' )


def transaction(request):
    name = request.user.id
    print(name)
    allhistory = Transhistory.objects.filter(user=name)

    context = {
        'allhistory' : allhistory
    }
    return render (request, 'funmizesub/transaction.html', context)


def services(request):
    return render (request, 'funmizesub/services.html' )


def airtime(request):
    return render (request, 'funmizesub/airtime.html' )

@csrf_exempt
def data(request):
    if request.method == 'POST':
        number = request.POST['number']
        plan = request.POST['plan']
        service = request.POST['service']        

        reffcode = str(uuid.uuid4())
        # reffcode = Math.floor((Math.random() * 1000000000) + 1)
        history = Transhistory(reference_id=refcode,card_number=number,volume=plan,service=service,amount=400,status='success',prebal=3500,postbal=3100,user=request.user)
        print(history.volume)
        print(refcode)
        history.save()
        # return redirect ('dashboard')
    # else :
        # print('no history found')
    # context = {
        # 'history' :history
    # }
    return render (request, 'funmizesub/dashboard.html')


def cable(request):
    return render (request, 'funmizesub/cable.html' )


def electricity(request):
    return render (request, 'funmizesub/electricity.html' )
    

def wallet(request):
    return render (request, 'funmizesub/wallet.html' )


def profile(request):
    # if request.method == 'POST':
        # username = request.POST['username']
        # email = request.POST['email']
        # phonenumber = request.POST['phonenumber']
        # status = request.POST['status']
        # referralid = request.POST['referralid']
        # bankname = request.POST['bankname']
        # acctname = request.POST['acctname']
        # acctnumber = request.POST['acctnumber']
# 
        # customerprofile = Customerprofile(username=username,email=email,phone_number=phonenumber,status=status,referral_id=referralid,bankname=bankname,acct_name=acctname,acct_number=acctnumber)
        # customerprofile.save()
        # messages.success(request, 'Thank you ' + ' ' + request.user.username + ' ' + 'Your profile has been updated successfully')
        ##messages.error(request,'There is something wrong with your input, please check through and get back to us!')
        # return redirect ('profile')
    # else:
        # print('am gettin bored')

    return render (request, 'funmizesub/profile.html' )

def sendmail(request):
    send_mail('Django Email','This a simply Email contest for test by Jelmah', 'jelmah00@gmail.com',['jelmah01@gmail.com'])
    return render(request, 'funmizesub/sendmail.html')

