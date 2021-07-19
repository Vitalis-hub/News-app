from django.shortcuts import render, get_object_or_404, redirect
from .models import Newsapp
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime
from subcat.models import SubCat
from cat.models import Cat
from trending.models import Trending
# Create your views here.

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

    return render(request, 'front/news_details.html', { 'site': site, 'news':newsapp, 'cat':cat, 'subcat': subcat, 'lastnews': lastnews, 'shownewsapp': shownewsapp, 'popnews':popnews, 'popnews2':popnews2, 'tag': tag, 'trending': trending})  #open the home page in html

def news_list(request):

    # login check start
    if not request.user.is_authenticated :
        return  redirect('mylogin')
    #login check end

    news = Newsapp.objects.all()
    

    return render(request, 'back/news_list.html', {'news': news})

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

                    b = Newsapp(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, date=today, picname = filename, picurl=url, writer='-', catname=newsname, catid=newsid, show=0, time=time, ocatid=ocatid, tag=tag)
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

    # login check start
    if not request.user.is_authenticated :
        return  redirect('mylogin')
    #login check end
    
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

            b.save()
            return redirect('news_list')

    return render(request, 'back/news_edit.html', {'pk': pk, 'news': news, 'cat': cat})