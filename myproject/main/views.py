from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from newsapp.models import Newsapp
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from trending.models import Trending
from django.contrib.auth.models import User
import random
from random import randint

# Create your views here.

def home(request):

    #check under post view
    #sitename = 'DjangoProject | Home'
    site = Main.objects.get(pk=1)
    sitename = site.name + " | Home"
    newsapp = Newsapp.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = Newsapp.objects.all().order_by('-pk')[:3]
    popnews = Newsapp.objects.all().order_by('-show')
    popnews2 = Newsapp.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]

    #get only top 5 trending (random system to extract record from project)
    random_object = Trending.objects.all()[randint(0, len(trending)-1)]
    print(random_object)

    return render(request, 'front/home.html', {'site': site, 'news':newsapp, 'cat':cat, 'subcat': subcat, 'lastnews': lastnews, 'popnews': popnews, 'popnews2':popnews2, 'trending': trending})  #open the home page in html


def inner_page(request):

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
    return render(request, 'back/home.html')


def mylogin(request):
    if request.method == 'POST':

        utxt = request.POST.get('username')
        ptxt = request.POST.get('password')

        if utxt != "" and ptxt != "":
            user = authenticate(username=utxt, password=ptxt)

            if user != None:
                login(request, user)
                return redirect('panel')


    return render(request, 'front/login.html')

def mylogout(reuest):

    logout(request)

    return redirect('mylogin')

def site_setting(request):

    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login check end


    if request.method == 'POST':
        name = request.POST.get('name')
        tell = request.POST.get('tell')
        fb = request.POST.get('fb')
        tw = request.POST.get('tw')
        yt = request.POST.get('yt')
        link = request.POST.get('link')
        txt = request.POST.get('txt')

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
        if picurl != "-": b.picurl = picurl
        if picname != "-": b.picname = picname
        if picurl2 != "-": b.picurl2 = picurl2
        if picname2 != "-": b.picname2 = picname2
        
        b.save()


        
    site = Main.objects.get(pk=2)

    return render(request, 'back/setting.html', {'site': site})

def about_setting(request):

     # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    #login check end

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

    return render(request, 'back/change_pass.html')