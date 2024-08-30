from django.shortcuts import render
from django.shortcuts import redirect
from web import models
from web.models import WangUser
# from web.forms import UserReg
# Create your views here.

def index(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        return render(request, 'index.html',param)
    else:
        return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_list = models.WangUser.objects.filter(username =username)

        error_name =[]
        if user_list:
            
            error_name = "The user name already exists"

            return render(request, {'error_name':error_name})
        else:
            username = models.WangUser.objects.create(username = username, password = password, email = email)
            username.save()

        return redirect('login')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')
        obj_user = models.WangUser.objects.filter(username=username, password=password)

        if obj_user:
            request.session['user'] = username
            request.session.set_expiry(10)
            return redirect('/index')
        else:
            error_name = 'user name and password invalid'
            return render(request, 'login.html',{'errorname':error_name})

    return render(request, 'login.html',locals())

def index(request):
    return render(request, 'index.html')

def logout(request):
    try:
        del request.session['user']

    except:
        return redirect('login')
    return redirect('login')