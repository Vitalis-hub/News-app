from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from newsapp.models import Newsapp
<<<<<<< HEAD
from newsletter.models import Newsletter
=======
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from trending.models import Trending
<<<<<<< HEAD
from django.contrib.auth.models import User, Group, Permission
from manager.models import Manager
import random
from random import randint
import string
from ipware import get_client_ip
from ip2geotools.databases.noncommercial import DbIpCity
from blacklist.models import Blacklist
from django.core.mail import send_mail
from django.conf import settings
from contactform.models import ContactForm
from zeep import Client
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
from rest_framework import viewsets
from .serializer import NewsSerializer
from django.http import JsonResponse

# Create your views here.

@csrf_exempt
def home(request):
    #try changing the port number using  python3 manage.py runserver 8080 to 8000
    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login check end
=======
from django.contrib.auth.models import User
import random
from random import randint

# Create your views here.

def home(request):
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c

    #check under post view
    #sitename = 'DjangoProject | Home'
    site = Main.objects.get(pk=1)
<<<<<<< HEAD
    newsapp = Newsapp.objects.filter().order_by('-pk')
=======
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
    sitename = site.name + " | Home"
    newsapp = Newsapp.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
<<<<<<< HEAD
    lastnews = Newsapp.objects.filter(act=1).order_by('-pk')[:3]
    popnews = Newsapp.objects.filter(act=1).order_by('-show')
    popnews2 = Newsapp.objects.filter(act=1).order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]
    lastnews2 = Newsapp.objects.filter(act=1).order_by('-show')[:4]
    '''
    #using soup and wstf method 
    # client = Client('********.wsdl')
    # result = client.service.funcname(1, 2,3)
    # print(result)

    #curl
    # url = '********************'
    # payload = {'a':'b', 'c':'d'}
    # result = requests.post(url, params=payload)
    # print(request.url)
    # print(request)

    # Json
    # url = '***************************************'
    # data = {'a':'b','c':'d'}
    # headers = {'Content Tpe': 'application/json', 'API_KEY': '***************************'}
    # result = requests.post(url, data=json.dumps(data), headers=headers)
    # print(result)

    
    #get only top 5 trending (random system to extract record from project)
    # random_object = Trending.objects.all()[randint(0, len(trending)-1)]
    # print(random_object)

    # my_html = """
    # <title> This is a Test </title>
    # """
    # soup = BeautifulSoup(my_html, 'html.parser')
    # print(soup.title)
    # print(soup.title.string)
    '''
    return render(request, 'front/home.html', {'site': site, 'news':newsapp, 'cat':cat, 'subcat': subcat, 'lastnews': lastnews, 'popnews': popnews, 'popnews2':popnews2, 'trending': trending, 'lastnews2':lastnews2})  #open the home page in html
=======
    lastnews = Newsapp.objects.all().order_by('-pk')[:3]
    popnews = Newsapp.objects.all().order_by('-show')
    popnews2 = Newsapp.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]

    #get only top 5 trending (random system to extract record from project)
    random_object = Trending.objects.all()[randint(0, len(trending)-1)]
    print(random_object)

    return render(request, 'front/home.html', {'site': site, 'news':newsapp, 'cat':cat, 'subcat': subcat, 'lastnews': lastnews, 'popnews': popnews, 'popnews2':popnews2, 'trending': trending})  #open the home page in html
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c


def inner_page(request):

<<<<<<< HEAD
    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login check end

=======
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
    site = Main.objects.get(pk=1)
    sitename = site.name + " | Home"
    newsapp = Newsapp.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = Newsapp.objects.all().order_by('-pk')[:3]
    popnews2 = Newsapp.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]

    site = Main.objects.get(pk=1)
    sitename = site.name + " | Inner_page"
    return render(request, 'front/inner_page.html', {'site': site, 'news':newsapp, 'cat':cat, 'subcat': subcat, 'lastnews': lastnews, 'popnews2':popnews2, 'trending': trending})

def panel(request):

    # login check start
    if not request.user.is_authenticated :
        return  redirect('mylogin')
    #login check end
<<<<<<< HEAD

    perm = 0
    perms = Permission.objects.filter(user=request.user)
    for i in perms :
        if i.codename == 'master_user': perm = 1
    
    '''
    test =['!', '0', '$', '%']
    rand = ""
    for i in range(4):
        rand = rand + random.choice(string.ascii_letters)
        rand += random.choice(test)
        rand += str(random.randint(0, 9))
    '''
    #number of news we have present
    # count = Newsapp.objects.count()
    # rand = Newsapp.object.all()[random.randint(0, count -1)]

    
    
    return render(request, 'back/home.html', {})
    
    
=======
    return render(request, 'back/home.html')
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c


def mylogin(request):
    if request.method == 'POST':

        utxt = request.POST.get('username')
<<<<<<< HEAD
        print("utxt", utxt)
        ptxt = request.POST.get('password')
        print(ptxt)

        if utxt != "" and ptxt != "":
            user = authenticate(username=utxt, password=ptxt)
            print(user)
=======
        ptxt = request.POST.get('password')

        if utxt != "" and ptxt != "":
            user = authenticate(username=utxt, password=ptxt)

>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
            if user != None:
                login(request, user)
                return redirect('panel')


    return render(request, 'front/login.html')

<<<<<<< HEAD
def register(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        print(name, uname, email, password1)

        if name == "":
            msg = "Input Your Name"
            return render(request, 'front/msgbox.html', {'msg': msg})

        if password1 != password2:
            msg = "Your Password Didn't Match"
            return render(request, 'front/msgbox.html', {'msg': msg})

        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0

        for i in password1:
            if i > '0' and i < '9':
                count1 = 1
            if i > 'A' and i < 'z':
                count2 = 1
            if i > 'a' and i < 'z':
                count3 = 1
            if i > '!' and i < '(':
               count4 = 1

        if count1 == 0 or count2 == 0 or count3 == 0 or  count4 == 0:
            msg = "Your Password id Not Strong"
            return render(request, 'front/msgbox.html', {'msg': msg})

        if len(password1) < 8:
            msg = "Your Password Must Be Atleast 8 Characters"
            return render(request, 'front/msgbox.html', {'msg': msg})

        #if the current password does not exist in the database. The password isn't a previous one
        if len(User.objects.filter(username=uname)) == 0 and len(User.objects.filter(email=email)) == 0:
            
            ip, is_routable = get_client_ip(request)

            if ip is None:
                ip = '0.0.0.0'

            try:
                response = DbIpCity.get(ip, api_key = 'free')
                country = response.country + ' | ' + response.city
            except:
                country = 'unknown'

            user = User.objects.create_user(username=uname, email=email, password=password1)
            b = Manager(name = name, utxt = uname, email=email, ip=ip, country=country)
            b.save()

    return render(request, 'front/register.html')

def mylogout(request):
=======
def mylogout(reuest):
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c

    logout(request)

    return redirect('mylogin')

def site_setting(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login check end

<<<<<<< HEAD
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1
    if perm == 0:
        error = "Access Denied"
        return render(request, "back/error.html", {'error': error})


=======
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c

    if request.method == 'POST':
        name = request.POST.get('name')
        tell = request.POST.get('tell')
        fb = request.POST.get('fb')
        tw = request.POST.get('tw')
        yt = request.POST.get('yt')
        link = request.POST.get('link')
        txt = request.POST.get('txt')
<<<<<<< HEAD
        seo_txt = request.POST.get('seotxt')
        seo_keywords = request.POST.get('seokeyword')
=======
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c

        if fb == "": fb = "#"
        if tw == "": tw = "#"
        if yt == "": yt = "==="

        if name == "" or tell == "" or txt == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error': error})

        try :
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            picurl = url
            picname = filename

        except:

            picurl = "-"
            picname = "-"

        
        try :
            myfile2 = request.FILES['myfile2']
            fs2 = FileSystemStorage()
            filename2 = fs2.save(myfile2.name, myfile2)
            url2 = fs2.url(filename2)

            picurl2 = url2
            picname2 = filename2

        except:

            picurl2 = "-"
            picname2 = "-"

        b = Main.objects.get(pk=2)
        b.name = name
        b.tell = tell
        b.fb = fb
        b.tw = tw
        b.yt = yt
        b.link = link
        b.about = txt
<<<<<<< HEAD

        b.seo_txt = seo_txt
        b.seo_keywords = seo_keywords
=======
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
        if picurl != "-": b.picurl = picurl
        if picname != "-": b.picname = picname
        if picurl2 != "-": b.picurl2 = picurl2
        if picname2 != "-": b.picname2 = picname2
        
        b.save()


        
<<<<<<< HEAD
    site = Main.objects.get(pk=1)
=======
    site = Main.objects.get(pk=2)
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c

    return render(request, 'back/setting.html', {'site': site})

def about_setting(request):

     # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login check end

<<<<<<< HEAD
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1
    if perm == 0:
        error = "Access Denied"
        return render(request, "back/error.html", {'error': error})


=======
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
    if request.method == 'POST':
        txt = request.POST.get('txt')

        if txt == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error': error})

        b = Main.objects.get(pk=1)
        b.abouttxt = txt
        b.save()

    about = Main.objects.get(pk=1).abouttxt

    return render(request, 'back/about_setting.html', {'about': about})

def contact(request):

    site = Main.objects.get(pk=1)
    sitename = site.name + " | Home"
    newsapp = Newsapp.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = Newsapp.objects.all().order_by('-pk')[:3]
    popnews2 = Newsapp.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:3]

    return render(request, 'front/contact.html', {'site': site, 'news':newsapp, 'cat':cat, 'subcat': subcat, 'lastnews': lastnews, 'popnews2':popnews2, 'trending': trending})

#changes password
def change_pass(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login check end

<<<<<<< HEAD
    if request.method == 'POST':

        oldpass = request.POST.get("oldpass")
        newpass = request.POST.get('newpass')
        if oldpass == "" or newpass == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error':error})

        user = authenticate(username=request.user, password=oldpass)
        if user != None:
            if len(newpass) < 8:
                error = "Your password must be at least eight characters"
                return render(request, "back/error.html", {'error': error})

            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0

            for i in newpass:
                if i > '0' and i < '9':
                    count1 = 1
                if i > 'A' and i < 'z':
                    count2 = 1
                if i > 'a' and i < 'z':
                    count3 = 1
                if i > '!' and i < '(':
                   count3 = 1
            
        if count1 == 1 and count2 == 1 and count3 == 1 and count4 ==1:
            user = User.objects.get(username=request.user)
            user.set_password(newpass)
            user.save()
            return redirect('mylogout')

        else:
            
            error = "Your Password is Not Correct"
            return render(request, "back/error.html", {'error': error})

    return render(request, 'back/change_pass.html')

def answer_cm(request, pk):

    if request.method == 'POST':
        txt = request.POST.get('txt')
        if txt == "":
            error = "Type your answer"
            return render(request, 'back/error.html', {'error': error} )

        to_email = ContactForm.objects.get(pk=pk).email

        '''
        subject = 'answer form'
        message = txt
        email_from = settings.EMAIL_HOST_USER
        emails = [to_email]
        send_mail(subject, message, email_from, emails)
        '''

        send_mail (
            'sender number 2',
            txt,
            'sender@djangolearn.xyz',
            [to_email],
            fail_silently = False
        )

    return render(request, 'back/answer_cm.html', {'pk': pk})


class NewsViewSet(viewsets.ModelViewSet):

    queryset = Newsapp.objects.all()
    serializer_class = NewsSerializer

def show_data(request):
    count = Newsletter.objects.filter(status=1).count()
    data = {'Count': count}
    return JsonResponse(data)
=======
    return render(request, 'back/change_pass.html')
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
