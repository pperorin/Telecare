from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from datastruct import views
from .models import dataDoctor,Disease
# Create your views here.


def home(request):
    return render(request, 'index.html')

def addForm(request):
    personnel = open('text/personnel.txt', 'r', encoding='utf8')
    name = personnel.readlines()
    name = name[0]
    personnel.close()
    if request.method == 'POST':
        date = request.POST['date']
        time = request.POST['time']
        symptom = request.POST['symptom']
        number = request.POST['number']
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
                    return render(request, 'addForm.html', {'press': 2})
        qform.enQ(date + '_' + time + '_' + symptom + '_' + number + '\n')
        ans = ''
        for i in qform.show():
            ans += i
        form = open('text/form.txt', 'w', encoding='utf8')
        form.write(ans)
        return render(request, 'addForm.html', {'press': 1})
    return render(request, 'addForm.html', {'name': name})


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        #f = open('text/user.txt', 'r', encoding='utf8')
        #s = f.readlines()
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
        f.close
        ans = username + ' ' + password + ' ' + fname + ' ' + lname + email + ' ' + '\n'
        f = open('text/user.txt', 'a', encoding='utf8')
        f.write(ans)
        f.close
        return render(request, 'signup.html', {'press': 2})  # ลงทะเบียนสำเร็จ
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
    return render(request, 'userInformation.html')

#รายชื่อโรค
def disease(request):
    datas = Disease.objects.all()
    return render(request, 'disease.html',{'datas':datas})


def about(request):
    return render(request, 'about.html')

