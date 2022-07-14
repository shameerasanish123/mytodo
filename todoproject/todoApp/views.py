from django.shortcuts import redirect, render
from . models import Register
from . models import Task

# Create your views here.
def register(request):
    return render(request,'register.html')

def register_form(request):
    if request.method =='POST':
        if Register.objects.filter(email_id=request.POST['email_id']):
            return render(request,'register.html',{'mail':"This mail id already registered with us !"})
        else:
            user_dis=Register(name=request.POST['name'],user_name=request.POST['user_name'],
                        email_id=request.POST['email_id'],phone_number=request.POST['phone_number'],
                        password=request.POST['password'],confirm_password=request.POST['confirm_password'])
            if user_dis.password == user_dis.confirm_password:  
                user_dis.save()
                return render(request,'register.html',{'msg':"Successfully Registered"})
            else:
                context={'pass':"password didn't match!"}
                return render(request,'register.html',context)
    else:
        return render(request,'register.html')

def login(request):
    if request.method=="POST":
        if Register.objects.filter(user_name=request.POST['user_name'],password=request.POST['password']).exists():
            user_display=Register.objects.get(user_name=request.POST['user_name'],password=request.POST['password'])
            return redirect(dashboard)
        else:
            context={'msg':"Username or Password is Wrong!"}
            return render(request,'login.html',context) 

    return render(request,'login.html')

def dashboard(request):
    if request.method=="POST":
        user_dis=Task(taskname=request.POST['taskname'],completed=request.POST['completed'],
                        date=request.POST['date'])
        user_dis.save()
        return redirect(dashboard_taskview)
    else:
        return render(request,'dashboard.html')

def dashboard_taskview(request):
    tasklist=Task.objects.all()
    return render(request,'dashboard.html',{'tasklist':tasklist})   

def editbook(request,id):
    edit1=Task.objects.get(id=id)
    return render(request,'update.html',{'edit1':edit1})

def updatebook(request,id):
    taskname=request.POST['taskname']
    completed=request.POST['completed']
    date=request.POST['date']
    edit1=Task.objects.filter(id=id).update(taskname=taskname,completed=completed,date=date)
    return redirect(dashboard_taskview)

def deletedata(request,id):
    var1=Task.objects.get(id=id)
    var1.delete()
    return redirect(dashboard_taskview)