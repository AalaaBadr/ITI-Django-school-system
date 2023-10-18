from django.contrib.auth.decorators import login_required
from django.shortcuts import *
from .forms import *
from django.contrib.auth import login, logout, authenticate


def logIn(req):
    context = {'form': LoginForm()}
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        obj = MyUser.objects.filter(username=username, password=password)
        authObj = authenticate(username=username, password=password)
        if len(obj) > 0 and authObj is not None:
            req.session['id'] = obj[0].id
            req.session['name'] = obj[0].username
            login(req, authObj)
            return redirect(reverse('home'))
        else:
            context['msg'] = 'invalid credentials'
    return render(req, 'myauth/login.html', context)


def logout(req):
    req.session.clear()
    return redirect(reverse('home'))


def register(req):
    context = {}
    context['form'] = Regform()

    context['form'] = RegistrationForm()
    if(req.method=='POST'):
        f = RegistrationForm(req.POST)
        if(f.is_valid()):
            f.save()#store user account_myuser
            User.objects.create_user(username=req.POST['username'],password=req.POST['username'],email='asd@yahii.com',is_staff=True)
            return redirect(reverse('login'))

    # if req.method == 'POST':
    #     f = Regform(req.POST)
    #     if f.is_valid():
    #         f.save()
    #         return redirect(reverse('home'))
    return render(req, 'myauth/register.html', context)


@login_required
def home(req):
    return render(req, 'index.html')
