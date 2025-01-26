from django.shortcuts import render, redirect
from jobs.models import Job
from myteam.models import Team
from contact.models import Contact
from login.models import Login
from apply.models import Apply
from signin.models import Signin
from donate.models import Donate
def login(request):
    if request.method == 'POST':
        email1=request.POST['myemail']
        passw=request.POST['password']
        x=Signin.objects.all().filter(signin_email=email1,signin_password=passw)
        if x.exists():
            #return redirect('/success1')
            return render(request,"success1.html")
    else:
        return render(request,"login.html")
def success1(request):
    em=request.GET['email']
    pas=request.GET['password']
    Login.objects.create(login_email=em,login_password=pas)
    return render(request,"success1.html")
def signup(request):
    return render(request,"signup.html")
def success2(request):
    nm=request.GET['name']
    em=request.GET['email']
    pas=request.GET['password']
    Signin.objects.create(signin_name=nm,signin_email=em,signin_password=pas)
    return render(request,"success2.html")
def dashboard(request):
    return render(request,"dashboard.html")
def about(request):
    return render(request,"about.html")
def event(request):
    return render(request,"events.html")
def explore(request):
    return render(request,"explore.html")
def resources(request):
    return render(request,"resources.html")
def contact(request):
    return render(request,"contact.html")
def success(request):
    fn=request.GET['name']
    em=request.GET['email']
    ph=request.GET['phone']
    ms=request.GET['message']
    Contact.objects.create(contact_name=fn,contact_email=em,contact_phone=ph,contact_messege=ms)
    return render(request,"success.html",{'name':fn})
def job(request):
    data=Job.objects.all()
    return render(request,"job.html",{'job_list':data})
def job_page(request,sid):
    data1=Job.objects.get(id=sid)
    return render(request,'job_details.html',{'details':data1})
def donate(request):
    return render(request,"donate.html")
def done(request):
    no=request.POST['mycard']
    ho=request.POST['holder']
    ex=request.POST['expiry']
    cv=request.POST['cvc']
    Donate.objects.create(donate_number=no,donate_holder=ho,donate_expiry=ex,donate_cvc=cv)
    return render(request,"done.html",{'holder':ho})
def apply(request):
    return render(request,"apply.html")
def confirm(request):
    fn=request.POST['fname']
    ln=request.POST['lname']
    em=request.POST['myemail']
    gn=request.POST['gender']
    pn=request.POST['code']
    ph=request.POST['phone']
    po=request.POST['age']
    dt=request.POST['dob']
    ad=request.POST['address']
    cv=request.POST['upload']
    name=fn+""+ln
    Apply.objects.create(apply_fname=fn,apply_lname=ln,apply_email=em,apply_gender=gn,apply_pincode=pn,apply_phone=ph,apply_position=po,apply_date=dt,apply_address=ad,apply_coverletter=cv)
    return render(request,"confirm.html",{'name':name})
def team(request):
    data2=Team.objects.all()
    return render(request,"team.html",{'team_list':data2})   
def team_page(request,sid):
    data3=Team.objects.get(id=sid)
    return render(request,'team_details.html',{'details':data3})
def user(request):
    return render(request,"login.html")