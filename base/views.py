from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.core.mail import send_mail

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create your views here.

def base(request):
    company_name = Company_name.objects.first()
    context = {'company_name':company_name}
    return render(request, 'base/home.html', context)

def position(request):
    company_name = Company_name.objects.first()
    if request.method == 'POST':
        try:
            tracking_id = request.POST['tracking_id']
            order = Order.objects.get(tracking_id = tracking_id)
            screen_width = request.POST['width']
            
            if int(screen_width) > 600:
                screen_width= 600

            order.screen_width = screen_width
            order.zoom = 1.0
            order.save()
            scr_width = str(order.screen_width)
            
            context={'order':order, 'scr_width':scr_width,'company_name':company_name}
            return render(request, 'base/position.html', context)
        except(KeyError, Order.DoesNotExist):
            err = 'We couldn\'t find the tracking information for this parcel. Please ensure the tracking ID is correct and hasn\'t already been fulfilled.'
            note = 'Please note that the tracking ID is case-sensitive. "OrDer1" is not the same as "oRdER1"'
            context={'company_name':company_name, 'err': err, 'note':note}
            return render(request, 'base/home.html', context)
    context={'order':order, 'scr_width':scr_width, 'company_name':company_name}
    return render(request, 'base/position.html', context)

def zoom(request, oti, zoomie):
    company_name = Company_name.objects.first()
    order = Order.objects.get(tracking_id = oti)
    if zoomie == "plus" and order.zoom<20:
        order.zoom = order.zoom + 0.5
        order.save()
        context = {'order':order, 'scr_width':order.screen_width, 'company_name':company_name}
        return render(request, 'base/position.html', context)
  
   
    if zoomie =="minus" and order.zoom >1:
        order.zoom= order.zoom - 0.5
        order.save()
        context = {'order':order, 'scr_width':order.screen_width, 'company_name':company_name}
        return render(request, 'base/position.html', context)
    else:
        err="MINIMUM/MAXIMUM ZOOM ACHIEVED"
        context = {'order':order, 'scr_width':order.screen_width, 'err':err, 'company_name':company_name}
        return render(request, 'base/position.html', context)
    

def quotes(request):
    company_name = Company_name.objects.first()
    if request.method == 'POST':
        ship_from = request.POST['from']
        ship_to = request.POST['to']
        weight = request.POST['weight']
        length = request.POST['length']
        width = request.POST['width']
        height = request.POST['height']
        email = request.POST['email']
        new_quote = Quote.objects.create(ship_from=ship_from,
                                          ship_to = ship_to, weight=weight,
                                          length=length, width=width,
                                            height= height, email=email)

        msg = 'Quote requested. We would get back to you as soon as possible.'
        context = {'msg':msg, 'company_name':company_name}
        return render(request, 'base/quotes.html', context)
    countries = Countries.objects.all()
    context = {'company_name':company_name, 'countries':countries}
    return render(request, 'base/quotes.html', context)

def new_shipment(request):
    company_name = Company_name.objects.first()
    countries = Countries.objects.all()
    context = {'company_name': company_name, 'countries':countries}
    return render(request, 'base/new-shipment.html', context)

def load_countries(request):
    countries = [
    "Argentina",
    "Australia",
    "Austria",
    "Belgium",
    "Brazil",
    "Canada",
    "China Mainland",
    "Colombia",
    "Costa Rica",
    "Czech Republic",
    "Denmark",
    "Dominican Republic",
    "Finland",
    "France",
    "Germany",
    "Greece",
    "Hong Kong SAR, China",
    "Hungary",
    "India",
    "Indonesia",
    "Ireland, Republic of",
    "Italy",
    "Japan",
    "Korea, South",
    "Luxembourg",
    "Macau SAR, China",
    "Malaysia",
    "Mexico",
    "Netherlands",
    "New Zealand",
    "Norway",
    "Philippines",
    "Poland",
    "Portugal",
    "Puerto Rico",
    "Romania",
    "Singapore",
    "South Africa",
    "Spain",
    "Sweden",
    "Switzerland",
    "Taiwan, China",
    "Thailand",
    "United Kingdom",
    "United States",
    "Vietnam"]
    for count in countries:
        c = Countries.objects.create(name = count)
        c.save()
    print('Countries loaded')


def billing(request):
    company_name = Company_name.objects.first()
    context  ={'company_name': company_name}
    return render(request, 'base/billing.html', context)

def login_request(request):
    company_name = Company_name.objects.first()

    if request.method == 'POST':
    
        if '@' in request.POST['username']:
            try:
                possible_user = User.objects.get(email = request.POST['username'])
            except(KeyError, User.DoesNotExist):
                possible_user = User.objects.get(username = request.POST['username'])
            user = authenticate(request, username = possible_user.username, password = request.POST['password'])
            print(possible_user.username)
            print(request.POST['password'])
            if user is not None:

                login(request, user)
                return HttpResponseRedirect(reverse('base:base'))
            else:
                msg = 'Invalid username or password.'
                context = {'company_name': company_name, 'msg': msg}
                return render(request, 'base/login.html', context)

        else:

            user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
            if user is not None:

                login(request, user)
                return HttpResponseRedirect(reverse('base:base'))
            else:
                msg = 'Invalid username or password.'
                context = {'company_name': company_name, 'msg': msg}
                return render(request, 'base/login.html', context)



    else:
        context  ={'company_name': company_name}
        return render(request, 'base/login.html', context)

def register(request):
    company_name = Company_name.objects.first()
    if request.method == 'POST':

        first_name = request.POST['first']
        last_name = request.POST['last']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone_number = request.POST['number']
        username = request.POST['username']

        if password1 == password2:
            try:

                new_user = User.objects.create_user(first_name = first_name, last_name = last_name, email = email, username = username, password= password1)
                new_user.save()
                Shipper.objects.create(first_name = first_name, last_name = last_name, user = new_user, phone_number = phone_number)
                login(request, new_user)
                return HttpResponseRedirect(reverse('base:base'))
            except(IntegrityError):
                context = {'msg': 'A user with this username already exists. Log in instead?', 'company_name': company_name}
                return render(request, 'base/signup.html', context)

        else:
            company_name = Company_name.objects.first()
            context = {'msg': 'Passwords do not match. Check and try again.', 'company_name': company_name}
            return render(request, 'base/signup.html', context)

    else:
        company_name = Company_name.objects.first()
        context  ={'company_name': company_name}
        return render(request, 'base/signup.html', context)
    
def logout_request(request):
    logout(request)
    return HttpResponseRedirect(reverse('base:base'))

def tracking(request):
    company_name = Company_name.objects.first()

    context = {'company_name':company_name}
    return render(request, 'base/tracking.html', context)

def profile(request):
    if request.user.is_authenticated:

        company_name = Company_name.objects.first()
        shipper = Shipper.objects.get(user = request.user)
        orders = Order.objects.filter(shipper = shipper)

        context = {'company_name': company_name, 'orders':orders}
        return render(request, 'base/profile.html', context)
    
    else:
        return HttpResponseRedirect(reverse('base:login'))
    
def pfp(request):

    if request.user.is_authenticated:
        if request.method == 'POST':
            photo = request.FILES['photo']
            request.user.shipper.pfp = photo
            request.user.shipper.save()
            return HttpResponseRedirect(reverse('base:profile'))
        else:
            request.user.shipper.pfp.delete()
            return HttpResponseRedirect(reverse('base:profile'))
    else:
        return HttpResponseRedirect(reverse('base:login'))
    
def mailer(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            email = request.POST['email']
            ranger = request.POST['range']
            try:

                send_mail(
                    "This is the test subject",
                    "Here is the general message",
                    "hello@dosojincargos.online",
                    [f'{email}'],
                    fail_silently=False
                )
            except Exception as e:
                MailError.objects.create(text = e, mail = email)
            
            return render(request, 'base/mailer.html')
        else:

            return render(request, 'base/mailer.html')
    else:
        context = {'err':'Only admin users can access this page. Please log in with your admin account.'}
        return render(request, 'base/login.html', context)