from django.shortcuts import render , HttpResponse , redirect
from . models import * 
def home(request):
    if request.session.has_key('user'):
        obj = rating.objects.all()
        n = rating.objects.count()
        sum = 0
        for i in obj:
            b = int(i.rate)
            sum = sum + b
        if sum == 0:
            sum = 0
        else:
            sum = sum / n
        name = request.session['user']
        return render(request,'view_rating.html',{'key':obj,'rating':sum , 'name':name})
    else:
        return redirect('login')

def rate(request):
    if request.session.has_key('user'):
        if request.method == 'POST':
            rate = request.POST.get('rate')
            message = request.POST.get('message')
            res = rating(name = request.session['user'],rate=rate,message=message)
            res.save()
            return redirect('home')
        else:
            name = request.session['user']
            exists = rating.objects.filter(name=name).exists()
            if(exists):
                return redirect('edit')
            else:
                return render(request,'rate.html')
    else:
        return redirect('login')
    
def edit(request):
    obj = rating.objects.get(name = request.session['user'])
    if request.method == 'POST':
        rate = request.POST.get('rate')
        message = request.POST.get('message')
        name = request.session['user']
        res = rating.objects.get(name = name)
        res.rate = rate
        res.message = message
        res.save()
        return redirect('home')
    return render(request,'edit.html',{'key': obj})

def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        exists = user.objects.filter(username=name).exists()
        if(exists):
            password = request.POST.get('password')
            obj = user.objects.get(username=name)
            if(obj.password == password):
                name = request.POST.get('name')
                request.session['user'] = name
                return redirect('home')
            else:
                return render(request,'login.html',{'key':f'Wrong Password for "{name}"'})

        else:
            return render(request,'login.html',{'key':'User Dose not Exist'})
    return render(request,'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        exists = user.objects.filter(username=name).exists()
        if(exists):
            return render(request,'signup.html',{'key':'Name Already exist'})
        else:
            obj = user(username = username , email = email , password = password)
            obj.save()
            return redirect('login')
    return render(request,'signup.html')


def logout(request):
    del request.session['user']
    return redirect('rate')