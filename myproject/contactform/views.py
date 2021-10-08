from django.shortcuts import render, get_object_or_404, redirect
from .models import ContactForm
from newsapp.models import Newsapp
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
import datetime
# Create your views here.

def contact_add(request):

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

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        sub = request.POST.get('subject')
        msg = request.POST.get('message')

        '''
        since our form is responsive and handles this case a different way there is no need to include this
        if name == "" or email == "" or msg == "":
            error = "All Fields Required"
            return render(request, 'front/msgbox.html', {'error': error}) 
        '''
    
        b = ContactForm(name=name, email = email, sub = sub, txt = msg, date =today, time = time)
        b.save()
        msg = "Your Message has been Sent"
        return render(request, 'front/msgbox.html', {'msg': msg})
    return render(request, 'front/msgbox.html')

def contact_show(request):

    # login check start
    if not request.user.is_authenticated :
        return  redirect('mylogin')
    #login check end

    msg = ContactForm.objects.all()

    return render(request, 'back/contact_form.html', {'msg': msg})

def contact_del(request, pk):

    # login check start
    if not request.user.is_authenticated :
        return  redirect('mylogin')
    #login check end

    b = ContactForm.objects.filter(pk=pk)
    b.delete()

    return redirect('contact_show')