
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Faculty,Student
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
def index(request):
       return render(request,'index.html',)
def registration(request):
       if request.method=='POST':
              err=None
              name=request.POST.get('name')
              gender=request.POST.get('gen')
              mobile=request.POST.get('mobile')
              dob=request.POST.get('dob')
              quali=request.POST.get('quali')
              email=request.POST.get('email')
              password=request.POST.get('password')
              data=Faculty(name=name,gender=gender,mobile=mobile,dob=dob,qualification=quali,password=password,username=email)              
              if Faculty.is_exist(email):
                     err="Email ! already exist.."
              if err:
                     return render(request,'registration.html',{'err':err}) 
              data.save()
              myuser=User.objects.create_user(username=email,password=password)
              myuser.save()
              return render(request,'index.html',{'msg':'Successfully registered ! Please login'})
       return render(request,'registration.html')
def signin(request):
       if request.method=='POST':
              id=request.POST.get('user')
              password=request.POST.get('password')
              myuser=authenticate(username=id,password=password)
              if myuser is not None:
                 login(request,myuser)
              
                 try:
                        faclt=Faculty.objects.filter(request.user.username)
                 except Exception as e:
                        print(e)
                        faclt=[]
                 request.session['faclt']=faclt
                 return redirect(mainpanel)
              else:
                     msg='Incorect Id or Password !!!'
                     render(request,'index.html',{'err':msg})
              
              
       return render(request,'index.html')
@login_required(redirect_field_name='index')
def panel(request):
       if request.method=='POST':
              name=request.POST.get('name')
              roll=request.POST.get('roll')
              course=request.POST.get('course')
              sem=request.POST.get('sem')
              branch=request.POST.get('branch')
              teacher=request.user.username
              stu=Student(name=name,rollno=roll,teacher=teacher,semester=sem,course=course,branch=branch)
              stu.save()

              return redirect(mainpanel)

       return render(request,'main.html')
@login_required(redirect_field_name='index')
def mainpanel(request):
       msg=None
       if  request.GET.get('flag')=='a':
              roll = request.GET.get('roll')
              abs = Student.objects.get(rollno=roll)
              Student.objects.filter(rollno=roll).update(absent=abs.absent + 1)
              msg=abs.name+" is absent"
       elif request.GET.get('flag')=='p':
              roll = request.GET.get('roll')
              prt = Student.objects.get(rollno=roll)
              Student.objects.filter(rollno=roll).update(present=prt.present + 1)
              msg=prt.name+" is present"
       fclt = Faculty.objects.get(username=request.user.username)
       stu = Student.objects.filter(teacher=request.user.username)
       data = {}
       data['stu'] = stu
       data['flt'] = fclt
       data['msg']=msg
       return render(request,'main.html',data)
@login_required(redirect_field_name='index')
def singout(request):
    logout(request)
    request.session.flush()
    return redirect('index')
@login_required(redirect_field_name='index')
def record(request):

    stu=Student.objects.filter(teacher=request.user.username)
    return render(request,'record.html',{'stu':stu})

@login_required(redirect_field_name='index')
def profile(request):
       flt=Faculty.objects.get(username=request.user.username)

       return render(request,'profile.html',{'flt':flt})