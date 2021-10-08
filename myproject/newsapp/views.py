from django.shortcuts import render, get_object_or_404, redirect
from .models import Newsapp
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime
from subcat.models import SubCat
from cat.models import Cat
from trending.models import Trending
<<<<<<< HEAD
import random
from comment.models import Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain

mysearch = ''
=======
# Create your views here.

>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
def news_detail(request,word):

    site = Main.objects.get(pk=1)
    sitename = site.name + " | Home"
    newsapp = Newsapp.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = SubCat.objects.all().order_by('-pk')[:3]


    #sitename = 'DjangoProject | Home'
    #site = Newsapp.objects.get(pk=1)
    shownewsapp = Newsapp.objects.filter(name=word)
    popnews = Newsapp.objects.all().order_by('-show')
    popnews2 = Newsapp.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]

    tagname = Newsapp.objects.get(name=word).tag
    tag = tagname.split(',')

    try :

        mynews = Newsapp.objects.get(name=word)
        mynews.show - mynews.show + 1
        mynews.save()

    except:
        print("Can't Add Show")
<<<<<<< HEAD
    
    code = Newsapp.objects.get(name=word).pk
    comment = Comment.objects.filter(news_id=code).order_by('-pk')[:3]
    cmcount = len(comment)

    link = "/urls/" + str(Newsapp.objects.get(name=word).rand)

    return render(request, 'front/news_details.html', { 'site': site, 'news':newsapp, 'cat':cat, 'subcat': subcat, 'lastnews': lastnews, 'shownewsapp': shownewsapp, 'popnews':popnews, 'popnews2':popnews2, 'tag': tag, 'trending': trending, 'code': code, 'comment': comment, 'cmcount': cmcount, 'link':link, 'tagname': tagname})  #open the home page in html


def news_detail_short(request,pk):

    site = Main.objects.get(pk=1)
    sitename = site.name + " | Home"
    newsapp = Newsapp.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = SubCat.objects.all().order_by('-pk')[:3]

    shownewsapp = Newsapp.objects.filter(rand=pk)
    popnews = Newsapp.objects.all().order_by('-show')
    popnews2 = Newsapp.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]

    tagname = Newsapp.objects.get(rand=pk).tag
    tag = tagname.split(',')

    try :

        mynews = Newsapp.objects.get(rand=pk)
        mynews.show - mynews.show + 1
        mynews.save()

    except:
        print("Can't Add Show")

    link = "/urls/" + str(Newsapp.objects.get(name=pk).rand)

    return render(request, 'front/news_details.html', { 'site': site, 'news':newsapp, 'cat':cat, 'subcat': subcat, 'lastnews': lastnews, 'shownewsapp': shownewsapp, 'popnews':popnews, 'popnews2':popnews2, 'tag': tag, 'trending': trending, 'link':link})  #open the home page in html



def news_list(request):

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1
        #did not have permission
    if perm == 0:
        news = Newsapp.objects.filter(writer=request.user)
        #main admin
    elif perm == 1:
        newss = Newsapp.objects.all()
        paginator = Paginator(newss, 2)
        page = request.GET.get('page')

        try:
            news = paginator.page(page)
        except EmptyPage:
            #send the next page or previous page
            news = paginator.page(paginator.num_page)
        except PageNotAnInteger:
            news = paginator.page(1)
    
=======

    return render(request, 'front/news_details.html', { 'site': site, 'news':newsapp, 'cat':cat, 'subcat': subcat, 'lastnews': lastnews, 'shownewsapp': shownewsapp, 'popnews':popnews, 'popnews2':popnews2, 'tag': tag, 'trending': trending})  #open the home page in html

def news_list(request):

>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
    # login check start
    if not request.user.is_authenticated :
        return  redirect('mylogin')
    #login check end
<<<<<<< HEAD
=======

    news = Newsapp.objects.all()
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
    

    return render(request, 'back/news_list.html', {'news': news})

<<<<<<< HEAD


=======
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
def news_add(request):

    # login check start
    if not request.user.is_authenticated :
        return  redirect('mylogin')
    #login check end

    print("--------------------------------------")
    
    now = datetime.datetime.now()
    print(now)
    year = now.year
    month = now.month
    day = now.day
    '''
    print(year, month, day)
    hour = now.hour
    minute = now.minute
    print(hour, minute)
    '''

    if len(str(day)) == 1:
        day = '0' + str(day)
    if len(str(month)) == 1:
        month = '0' + str(month)

    today = str(year) + "/" + str(month) + "/" + str(day)
    time = str(now.hour) + ":" + str(now.minute)

<<<<<<< HEAD
    date = str(year) + str(month) + str(day)
    randint = str(random.randint(1000, 9999))
    rand = date + randint
    rand = int(rand)

    while len(Newsapp.objects.filter(rand=rand)) != 0:
        randint = random.randint(1000, 9999)
        rand = date + randint
        rand = int(rand)

=======
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
    cat = SubCat.objects.all()
    print("--------------------------------------")
    

    #get he form posted
    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        newsid = request.POST.get('newscat')
        tag = request.POST.get('tag')

        #print(newstitle, newscat, newstxtshort, newstxt)
        print(newstxt)
        if newstitle == '' or newstxtshort == '' or newstxt == '' or newscat == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error': error})
        
        try :
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)
            
            if str(myfile.content_type).startswith("image"):
                
                if myfile.size < 5000000:

                    newsname = SubCat.objects.get(pk = newsid).catname
                    ocatid = SubCat.objects.get(pk=newsid).catid

<<<<<<< HEAD
                    b = Newsapp(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, date=today, picname = filename, picurl=url, writer=request.user, catname=newsname, catid=newsid, show=0, time=time, ocatid=ocatid, tag=tag, rand =rand)
=======
                    b = Newsapp(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, date=today, picname = filename, picurl=url, writer='-', catname=newsname, catid=newsid, show=0, time=time, ocatid=ocatid, tag=tag)
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
                    b.save()

                    count = len(Newsapp.objects.filter(ocatid=ocatid))

                    b = Cat.objects.get(pk=ocatid)
                    b.count = count
                    b.save()

                    return redirect('news_list')
                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)
                    
                    error = "Your File Is Bigger Than 5 MB"
                    return render(request, 'back/error.html', {'error': error})
            else:
                fs = FileSystemStorage()
                fs.delete(filename)

                error = "Your File Not Supported"
                return render(request, 'back/error.html', {'error': error})
        except:

            error = "Please input your image"
            return render(request, 'back/error.html', {'error': error})
    return render(request, 'back/news_add.html', {'cat': cat})

def news_delete(request, pk):

    # login check start
    if not request.user.is_authenticated :
        return  redirect('mylogin')
    #login check end

<<<<<<< HEAD
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1
    if perm == 0:
       a = Newsapp.objects.get(pk=pk).writer
       if str(a) != str(request.user):
           error = "Access Denied"
           return render(request, 'back/error.html', {'error': error})

=======
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
    try:
        b = Newsapp.objects.get(pk=pk)

        #deleting the image and then deleting the query itself
        fs = FileSystemStorage()
        fs.delete(b.picname)
        ocatid = Newsapp.objects.get(pk=pk).ocatid
        b.delete()

        count = len(Newsapp.objects.filter(ocatid=ocatid))

        n = Cat.objects.get(pk=ocatid)
        n.count = count
        n.save()

    except:
        error = "Something Wrong"
        return render(request, 'back/error.html', {'error': error})

    return redirect("news_list")

def news_edit(request, pk):
<<<<<<< HEAD
    
=======

>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
    # login check start
    if not request.user.is_authenticated :
        return  redirect('mylogin')
    #login check end
<<<<<<< HEAD

    perm = 0
    for i in request.user.groups.all():
        if i.name == 'masteruser': perm = 1
    if perm == 0:
        a = Newsapp.objects.get(pk=pk).writer
        if a != request.user:
            error = "Access Denied"
            return render(request, 'back/error.html', {'error': error})

=======
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
    
    if len(Newsapp.objects.filter(pk=pk)) == 0:
        error = "News Not Found"
        return render(request, 'back/error.html', {'error': error})
    
    news = Newsapp.objects.get(pk=pk)
    cat = SubCat.objects.all()

    #get he form posted
    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        newsid = request.POST.get('newscat')
        tag = request.POST.get('tag')

        #print(newstitle, newscat, newstxtshort, newstxt)
        print(newstxt)
        if newstitle == '' or newstxtshort == '' or newstxt == '' or newscat == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error': error})
        
        try :
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)
            
            if str(myfile.content_type).startswith("image"):
                
                if myfile.size < 5000000:

                    newsname = SubCat.objects.get(pk = newsid).name
                    
                    b = Newsapp.objects.get(pk=pk)

                    fss = FileSystemStorage()
                    fss.delete(b.picname)

                    b.name = newstitle
                    b.short_txt = newstxtshort
                    b.body_txt = newstxt
                    b.picname = filename
                    b.picurl = url
                    b.catname = newsname
                    b.catid = newsid
                    b.tag = tag

                    b.save()
                    return redirect('news_list')
                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)
                    
                    error = "Your File Is Bigger Than 5 MB"
                    return render(request, 'back/error.html', {'error': error})
            else:
                fs = FileSystemStorage()
                fs.delete(filename)

                error = "Your File Not Supported"
                return render(request, 'back/error.html', {'error': error})
        except:

            newsname = SubCat.objects.get(pk = newsid).name
                    
            b = Newsapp.objects.get(pk=pk)
            b.name = newstitle
            b.short_txt = newstxtshort
            b.body_txt = newstxt
            b.catname = newsname
            b.catid = newsid
            b.tag = tag
<<<<<<< HEAD
            b.act = 0
=======
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c

            b.save()
            return redirect('news_list')

<<<<<<< HEAD
    return render(request, 'back/news_edit.html', {'pk': pk, 'news': news, 'cat': cat})

def news_publish(request, pk):

    # login check start
    if not request.user.is_authenticated :
        return  redirect('mylogin')
    #login check end

    newsapp = Newsapp.objects.get(pk=pk)
    newsapp.act = 1
    newsapp.save()

    return redirect("news_list")

def news_all_show(request, word):
    
    catid = Cat.objects.get(name=word).pk
    anews = Newsapp.objects.filter(ocatid=catid)

    site = Main.objects.get(pk=1)
    allnewsapp = Newsapp.objects.filter().order_by('-pk')
    sitename = site.name + " | Home"
    newsapp = Newsapp.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = Newsapp.objects.filter(act=1).order_by('-pk')[:3]
    popnews = Newsapp.objects.filter(act=1).order_by('-show')
    popnews2 = Newsapp.objects.filter(act=1).order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]
    lastnews2 = Newsapp.objects.filter(act=1).order_by('-show')[:4]

    
    return render(request, 'front/all_news.html', {'site': site, 'news':newsapp, 'cat':cat, 'subcat': subcat, 'lastnews': lastnews, 'popnews': popnews, 'popnews2':popnews2, 'trending': trending, 'lastnews2':lastnews2, 'allnewsapp':allnewsapp})  #open the home page in html


def all_news(request):
    allnews = Newsapp.objects.all()
    site = Main.objects.get(pk=1)
    allnewsapp = Newsapp.objects.filter().order_by('-pk')
    sitename = site.name + " | Home"
    newsapp = Newsapp.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = Newsapp.objects.filter(act=1).order_by('-pk')[:3]
    popnews = Newsapp.objects.filter(act=1).order_by('-show')
    popnews2 = Newsapp.objects.filter(act=1).order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]
    lastnews2 = Newsapp.objects.filter(act=1).order_by('-show')[:4]

    
    now = datetime.datetime.now()
    print(now)
    year = now.year
    month = now.month
    day = now.day
    '''
    print(year, month, day)
    hour = now.hour
    minute = now.minute
    print(hour, minute)
    '''

    if len(str(day)) == 1:
        day = '0' + str(day)
    if len(str(month)) == 1:
        month = '0' + str(month)

    today = str(year) + "/" + str(month) + "/" + str(day)
    f_rom = []
    t_o = []

    for i in range(30):
        b = datetime.datetime.now() + datetime.timedelta(days=i)
        year = b.year
        month = b.month
        day = b.day
        '''
        print(year, month, day)
        hour = now.hour
        minute = now.minute
        print(hour, minute)
        '''

        if len(str(day)) == 1:
            day = '0' + str(day)
        if len(str(month)) == 1:
            month = '0' + str(month)
        b = str(year) + "/" + str(month) + "/" + str(day)
        f_rom.append(b)

    for i in range(30):
        b = datetime.datetime.now() + datetime.timedelta(days=i)
        year = b.year
        month = b.month
        day = b.day
        '''
        print(year, month, day)
        hour = now.hour
        minute = now.minute
        print(hour, minute)
        '''

        if len(str(day)) == 1:
            day = '0' + str(day)
        if len(str(month)) == 1:
            month = '0' + str(month)
        b = str(year) + "/" + str(month) + "/" + str(day)
        t_o.append(b)

    return render(request, 'front/all_news.html', {'site': site, 'news':newsapp, 'cat':cat, 'subcat': subcat, 'lastnews': lastnews, 'popnews': popnews, 'popnews2':popnews2, 'trending': trending, 'lastnews2':lastnews2, 'allnewsapp':allnewsapp, 'allnews': allnews, 'f_rom':f_rom, 't_o':t_o})  #open the home page in html

def all_news_search(request):
    global mysearch
    catid = '0'
    if request.method == "POST":
        txt = request.POST.get('txt')
        catid = request.POST.get('cat')
        f_rom = request.POST.get('f_rom')
        t_o = request.POST.get('t_o')

        if f_rom != '0' and t_o != '0':
            if t_o < f_rom:
                error = 'You did not specify the correct range for date'
                return render(request, 'front/msgbox.html', {'error':error})
        mysearch = txt
        if catid == '0':
            if f_rom != '0' and t_o != '0':
                a = Newsapp.objects.filter(name__contains=txt, date__gte=f_rom, date__lte=t_o)
                b = Newsapp.objects.filter(short_txt__contains=txt, date__gte=f_rom, date__lte=t_o)
                c = Newsapp.objects.filter(body_txt__contains=txt, date__gte=f_rom, date__lte=t_o)
            elif f_rom != '0':
                a = Newsapp.objects.filter(name__contains=txt, date__gte=f_rom)
                b = Newsapp.objects.filter(short_txt__contains=txt, date__gte=f_rom)
                c = Newsapp.objects.filter(body_txt__contains=txt, date__gte=f_rom)
            elif t_o != '0':
                a = Newsapp.objects.filter(name__contains=txt, date__lte=t_o)
                b = Newsapp.objects.filter(short_txt__contains=txt, date__lte=t_o)
                c = Newsapp.objects.filter(body_txt__contains=txt, date__lte=t_o)
            else:
                a = Newsapp.objects.filter(name__contains=txt)
                b = Newsapp.objects.filter(short_txt__contains=txt)
                c = Newsapp.objects.filter(body_txt__contains=txt)
        else:
            if f_rom != '0' and t_o != '0':
                a = Newsapp.objects.filter(name__contains=txt, ocatid=catid, date__gte=f_rom, date__lte=t_o)
                b = Newsapp.objects.filter(short_txt__contains=txt, ocatid=catid, date__gte=f_rom, date__lte=t_o)
                c = Newsapp.objects.filter(body_txt__contains=txt, ocatid=catid, date__gte=f_rom, date__lte=t_o)
            else:
                a = Newsapp.objects.filter(name__contains=txt, ocatid=catid)
                b = Newsapp.objects.filter(short_txt__contains=txt, ocatid=catid)
                c = Newsapp.objects.filter(body_txt__contains=txt, ocatid=catid)
        allnewss = list(chain(a,b,c))
        allnewss =list(dict.fromkeys(allnewss))
        
    else:
        if catid == '0':
            if f_rom != '0' and t_o != '0':
                a = Newsapp.objects.filter(name__contains=mysearch,  date__gte=f_rom, date__lte=t_o)
                b = Newsapp.objects.filter(short_txt__contains=mysearch,  date__gte=f_rom, date__lte=t_o)
                c = Newsapp.objects.filter(body_txt__contains=mysearch,  date__gte=f_rom, date__lte=t_o)
            elif f_rom != '0':
                a = Newsapp.objects.filter(name__contains=mysearch,  date__gte=f_rom)
                b = Newsapp.objects.filter(short_txt__contains=mysearch,  date__gte=f_rom)
                c = Newsapp.objects.filter(body_txt__contains=mysearch,  date__gte=f_rom)
            elif t_o != '0':
                a = Newsapp.objects.filter(name__contains=mysearch,  date__gte=t_o)
                b = Newsapp.objects.filter(short_txt__contains=mysearch,  date__gte=t_o)
                c = Newsapp.objects.filter(body_txt__contains=mysearch,  date__gte=t_o)
            else:
                a = Newsapp.objects.filter(name__contains=mysearch)
                b = Newsapp.objects.filter(short_txt__contains=mysearch)
                c = Newsapp.objects.filter(body_txt__contains=mysearch)
        else:
            if f_rom != '0' and t_o != '0':
                a = Newsapp.objects.filter(name__contains=txt, ocatid=catid,  date__gte=f_rom, date__lte=t_o)
                b = Newsapp.objects.filter(short_txt__contains=txt, ocatid=catid, date__gte=f_rom, date__lte=t_o)
                c = Newsapp.objects.filter(body_txt__contains=txt, ocatid=catid, date__gte=f_rom, date__lte=t_o)
            elif f_rom != '0':
                a = Newsapp.objects.filter(name__contains=txt, ocatid=catid,  date__gte=f_rom)
                b = Newsapp.objects.filter(short_txt__contains=txt, ocatid=catid, date__gte=f_rom)
                c = Newsapp.objects.filter(body_txt__contains=txt, ocatid=catid, date__gte=f_rom)
            elif t_o != '0':
                a = Newsapp.objects.filter(name__contains=txt, ocatid=catid, date__lte=t_o)
                b = Newsapp.objects.filter(short_txt__contains=txt, ocatid=catid, date__lte=t_o)
                c = Newsapp.objects.filter(body_txt__contains=txt, ocatid=catid, date__lte=t_o)
            else:
                a = Newsapp.objects.filter(name__contains=txt, ocatid=catid)
                b = Newsapp.objects.filter(short_txt__contains=txt, ocatid=catid)
                c = Newsapp.objects.filter(body_txt__contains=txt, ocatid=catid)
        allnewss = list(chain(a,b,c))
        allnewss =list(dict.fromkeys(allnewss))

    site = Main.objects.get(pk=1)
    allnewsapp = Newsapp.objects.filter().order_by('-pk')
    sitename = site.name + " | Home"
    newsapp = Newsapp.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = Newsapp.objects.filter(act=1).order_by('-pk')[:3]
    popnews = Newsapp.objects.filter(act=1).order_by('-show')
    popnews2 = Newsapp.objects.filter(act=1).order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]
    lastnews2 = Newsapp.objects.filter(act=1).order_by('-show')[:4]

    paginator = Paginator(allnewss,12)
    page = request.GET.get('page')

    try:
        allnews = paginator.page(page)

    except EmptyPage:
        allnews = paginator.page(paginator.num_page)
    except PageNotAnInteger:
        allnews = paginator.page(1)
    
    return render(request, 'front/all_news.html', {'site': site, 'news':newsapp, 'cat':cat,'subcat': subcat, 'lastnews': lastnews, 'popnews': popnews, 'popnews2':popnews2, 'trending': trending, 'lastnews2':lastnews2, 'allnewsapp':allnewsapp, 'allnews': allnews, 'f_rom': f_rom, 't_o':t_o})  #open the home page in html


b = Newsapp.objects.filter(date__gte='2019/01/01')
b = Newsapp.objects.filter(date__lte='2019/01/01')

=======
    return render(request, 'back/news_edit.html', {'pk': pk, 'news': news, 'cat': cat})
>>>>>>> 2835b47b2b661218de4bf07d459eab63127e891c
