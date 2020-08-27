from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views import View

from . import models
from news.models import News
from category.models import Category


def home(request):
    site = models.Main.objects.get(pk=1)
    news_list = News.objects.all().order_by('-created_date')
    categories = Category.objects.all()
    return render(
        request, 'front/home.html',
        {'site': site, 'news_list': news_list, 'categories': categories}
    )


def about(request):
    site = models.Main.objects.get(pk=1)
    categories = Category.objects.all()
    news_list = News.objects.all().order_by('-created_date')

    return render(request, 'front/about.html', {'site': site, 'categories': categories, 'news_list': news_list})


@login_required()
def panel(request):
    return render(request, 'back/home.html')


def admin_login(request):
    if request.method == 'POST':
        username = request.POST['login-username']
        password = request.POST['login-password']

        if username == '' or password == '':
            return render(request, 'front/login.html', {'error': 'Please fill all fields.'})

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            redirect_url = request.GET.get('next')
            print(redirect_url)
            return HttpResponseRedirect(redirect_url)
        else:
            return render(request, 'front/login.html', {'error': 'Provided Credentials is wrong.'})
    return render(request, 'front/login.html')


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('login')


def site_setting(request):
    setting = get_object_or_404(models.Main, pk=1)
    if request.method == 'POST':
        name = request.POST['name']
        set_name = request.POST['set_name']
        phone_number = request.POST['phone_number']
        link = request.POST['link']
        facebook = request.POST['facebook']
        twitter = request.POST['twitter']
        youtube = request.POST['youtube']

        if link == '':
            link = '#'
        if twitter == '':
            twitter = '#'
        if facebook == '':
            facebook = '#'
        if youtube == '':
            youtube = '#'

        if name == '' or set_name == '' or phone_number == '':
            return render(request, 'back/settings.html', {'setting': setting, 'error': 'Please fill required fields.'})

        setting.__dict__.update(
            {
                'name': name,
                'set_name': set_name,
                'phone_number': phone_number,
                'link': link,
                'facebook': facebook,
                'twitter': twitter,
                'youtube': youtube
            }
        )
        setting.save()
        return redirect('site_setting')
    return render(request, 'back/settings.html', {'setting': setting})

