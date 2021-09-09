from django.shortcuts import render,redirect
from . models import *
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'index.html')
def fnhome(request):
    return render(request,'home.html')

def fnad_home(request):
    return render(request,'ad-home.html')
def fnad_login(request):
    
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        loginobj=Login.objects.get(username=username,password=password)
        if(username=='admin'):
            request.session['logid']=loginobj.id
            return render(request,"ad-home.html")
    return render(request,"ad-login.html")
def fnadmin_logout(request):
    try:
        del request.session['logid']
    except:
        return render(request,"home.html")
    return render(request,"home.html")

def fnuser_login(request):
    if(request.method=='POST'):
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            loginobj=Login.objects.get(username=username,password=password)
            if(username!='admin'):
                request.session['logid']=loginobj.id
                return render(request,"user-home.html")
        except Exception as e:
            return render(request,"user-login.html")
    else:
        return render(request,'user-login.html')

def fnuser_logout(request):
    try:
        del request.session['logid']
    except:
        return render(request,'home.html')
    return render(request,'home.html')
    
def fnuser_reg(request):
    return render(request,'user-reg.html')
    
def fnuser_registration(request):
    if(request.method=='POST'):
        name=request.POST.get('name')
        contact=request.POST.get('phone')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        loginobj=Login(username=username,password=password)
        loginobj.save()
        regobj=Registration(name=name,contact=contact,email=email,user_id=loginobj)
        regobj.save()
        status="Active"
        statusobj=Studentstatus(stud=regobj,user_log=loginobj,status=status)
        statusobj.save()
        return render(request,'user-reg.html')
    else:
        return render(request,'ad-login.html')
    return render(request,'user_registration.html')
    
def fnstatus_stud(request):
    i=int(request.POST.get('status'))
    statusobj=Status.objects.get(id=i)
    status=statusobj.status
    if status=="Active":
        statusobj.status="Inactive"
        statusobj.save()
        active=Status.objects.filter(status="Active")
        if active:
            return render(request,'active-stud.html',{'active':active})
        else:
            return render(request,'active-stud.html')
    elif status=="Inactive":
        statusobj.status="Active"
        statusobj.save()
        inactive=Status.objects.filter(status="Inactive")
        if inactive:
            return render(request,'inactive-stud.html',{'inactive':inactive})
        else:
            return render(request,'inactive-stud.html')
    return render(request,'ad-home.html')

def fnactive_stud(request):
    try:
        if request.session['logid']:
            active=Studentstatus.objects.filter(status="Active")
            loginobj=Login.objects.all()
            if active:
                return render(request,'active-stud.html',{'active':active})
            return render(request,'active-stud.html')
            
    except Exception as e:
        return redirect('ad-login')
    return redirect('ad-login')
    

def fninactive_stud(request):
    try:
        if request.session['logid']:
            inactive=Studentstatus.objects.filter(status="Inactive")
            loginobj=Login.objects.all()
            if inactive:
                return render(request,'inactive-stud.html',{'inactive':inactive})
            return render(request,'inactive-stud.html')
    except Exception as e:
        return redirect('ad-login')
    return redirect('ad-login')


def fnuser_home(request):
    id=request.session['logid']
    regobj=Registration.objects.get(user_id=id) 
    return render(request,"user-home.html",{'reg':regobj})
    
def fnview_profile(request):
    id=request.session['logid']
    regobj=Registration.objects.get(user_id=id)    
    return render(request,'view-profile.html',{'reg':regobj})

def fnupdate_profile(request):
    if request.session['logid']:
        id=request.session['logid']
        loginobj=Login.objects.get(id=id)
        regobj=Registration.objects.get(user_id=loginobj) 
        statusobj=Studentstatus.objects.get(user_log=loginobj)
        if(request.method=='POST'):
            name=request.POST.get('name')
            contact=request.POST.get('phone')
            email=request.POST.get('email')
            username=request.POST.get('username')
            password=request.POST.get('password')
            regobj.name=name
            regobj.contact=contact
            regobj.email=email
            regobj.save()
            loginobj.username=username
            loginobj.password=password
            loginobj.save()
            return render(request,'update-profile.html',{'reg':regobj,'status':statusobj})
        return render(request,'update-profile.html',{'reg':regobj,'status':statusobj})
    return render(request,'update-profile.html')
    

   

