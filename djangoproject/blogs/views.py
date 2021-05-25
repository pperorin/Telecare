from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib import messages
from datastruct import views
from .models import dataDoctor,Disease
# Create your views here.


def home(request):
    return render(request, 'index.html')

def addForm(request):
    if request.method == 'POST':
        name=request.user.first_name
        date = request.POST['date']
        time = request.POST['time']
        symptom = request.POST['symptom']
        number = request.POST['number']
        if date=='' or time=='':
            messages.info(request,'โปรดใส่วันเวลา')
            return render(request, 'addForm.html')
        #localtime = time.localtime(1623742123)
        form = open('text/form.txt', 'r', encoding='utf8')
        sform = form.readlines()
        form.close()
        qform = views.Queue()
        for i in sform:  # list แต่ละบรรทัด
            j = i.split('_')  # list แต่ละหัวข้อ  j[0]:date    j[1]:time
            qform.enQ(i)
            if j[0] == date:
                if j[1] == time:
                    # คิวที่จะจองเต็ม
                    messages.info(request,'คิวเต็ม')
                    return render(request, 'addForm.html')
        qform.enQ(date + '_' + time + '_' + name + '_' + number + '_' + symptom + '\n')
        sort=views.sorting()
        sort.sortDate(qform.show())
        ans = ''
        for i in qform.show():
            ans += i
        form = open('text/form.txt', 'w', encoding='utf8')
        form.write(ans)
        return render(request, 'addForm.html')
    return render(request, 'addForm.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        if password == repassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username นี้มีคนใช้แล้ว')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email นี้เคยลงทะเบียนไว้แล้ว')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    first_name=fname,
                    last_name=lname,
                    email=email,
                )
                user.save()
                return redirect('/home')
        else:
            messages.info(request,'รหัสผ่านไม่ตรงกัน')
            return render(request, 'signup.html')
        ans = username + ' ' + password + ' ' + fname + ' ' + lname + email + ' ' + '\n'
        return render(request, 'signup.html')  # ลงทะเบียนสำเร็จ
    return render(request, 'signup.html')  # เข้าหน้าเว็บปกติ


def signin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        #login
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/home')
        else:
            messages.info(request,'ไม่พบข้อมูล')
            return redirect('/')
    return render(request, 'signin.html')


def check(request):
    return render(request, 'check.html')

#รายชื่อหมอ
def personnel(request):
    datas = dataDoctor.objects.all()
    return render(request, 'personnel.html', {'datas': datas})


def userInformation(request):
    name=request.user.first_name
    form = open('text/form.txt', 'r', encoding='utf8')
    strform = form.readlines()
    form.close()
    stack=views.Stack()
    dates=[]
    times=[]
    symptom=[]
    datas=[]
    ans=[]
    for i in range(len(strform)-1,-1,-1):
        if strform[i].split('_')[2] == name:
            stack.push(strform[i])
    while stack.lst!=[]:
        data=list(stack.peek().split("_"))
        dates.append(data[0])
        times.append(data[1])
        symptom.append(data[4])
        stack.pop()
    for i in range(len(dates)):
        datas.append(dates[i] + ' ' + times[i] + ' ' + symptom[i])
    if request.method =="POST":
        checkdate=request.POST['date']
        if checkdate != '':
            for i in datas:
                date=i.split(' ')[0]
                #เช็ควันที่จอง
                if date == checkdate:
                    ans.append(i)
            if len(ans)>1:
                return render(request, 'userInformation.html',{'datas':ans,'press':0})
            elif len(ans)>0:
                return render(request, 'userInformation.html',{'datas':ans[0],'press':1})
            else:
                return render(request, 'userInformation.html',{'press':2})
        else:
            return render(request, 'userInformation.html',{'press':3})
    #มีdata หลายตัว
    elif len(datas)>1:
        return render(request, 'userInformation.html',{'datas':datas,'press':0})
    elif len(datas)>0:
        return render(request, 'userInformation.html',{'datas':datas[0],'press':1})
    else:
        return render(request, 'userInformation.html',{'press':2})
        
def about(request):
    return render(request, 'about.html')

#รายชื่อโรค
def disease(request):
    datas = Disease.objects.all()
    return render(request, 'disease.html',{'datas':datas})

#All Disease
def bone(request):
    return render(request, 'bone.html')
def cancer(request):
    return render(request, 'cancer.html')
def heart(request):
    return render(request,'heart.html')
def dental(request):
    return render(request,'dental.html')
def digestivesystem(request):   #ทางเดินอาหาร
    return render(request,'digestivesystem.html')
def pediatric(request):         #โรคในเด็ก
    return render(request,'pediatric.html')
def brain(request):
    return render(request,'brain.html')
