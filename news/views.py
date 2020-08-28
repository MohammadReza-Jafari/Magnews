from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import os

from . import models
from main.models import Main
from subcategory.models import Subcategory
from news.models import News
from category.models import Category


def news_details(request, title):
    site = Main.objects.get(pk=1)
    news = get_object_or_404(models.News, title=title)
    news_set = News.objects.all().order_by('-created_date')
    categories = Category.objects.all()
    return render(
        request, 'news/news_details.html',
        {'news': news, 'site': site, 'news_list': news_set, 'categories': categories}
    )


@login_required()
def news_list(request):
    news = models.News.objects.all().order_by('-created_date')
    return render(request, 'back/news_list.html', {'news_list': news})


@login_required()
def add_news(request):
    subcategories = Subcategory.objects.all()
    if request.method == 'POST':
        error_messages = []
        image = None
        title = request.POST['title']
        description = request.POST['description']
        selected_category = request.POST['selected_subcategory']
        body = request.POST['body']
        if title == '' or description == '' or selected_category == '' or body == '' or len(request.FILES) == 0:
            error_messages.append('All Fields Required.')

        if len(request.FILES) > 0:
            image = request.FILES['image']
            if not str(image.content_type).startswith('image'):
                error_messages.append('Your File Type Not Supported, Choose An Image.')
            else:
                if image.size > 4000000:
                    error_messages.append('Your Image Must Be Smaller Than 4 MB.')

        if len(error_messages) > 0:
            return render(request, 'back/add_news.html', {'errors': error_messages, 'subcategories': subcategories})

        news = models.News(
            title=title,
            description=description,
            subcategory_id=selected_category,
            body=body,
            image=image,
            author='cloner',
            views=100
        )
        news.save()
        category = news.subcategory.category
        category.count += 1
        category.save()
        return redirect('news:list')
    return render(request, 'back/add_news.html', {'subcategories': subcategories})


@login_required()
def delete_news(request, pk):
    news = get_object_or_404(models.News, pk=pk)
    if os.path.exists(news.image.path):
        os.remove(news.image.path)

    category = news.subcategory.category;
    category.count -= 1
    category.save()
    news.delete()
    return redirect('news:list')


@login_required()
def edit_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    subcategories = Subcategory.objects.all()
    if request.method == 'POST':
        error_messages = []
        image = None
        title = request.POST['title']
        description = request.POST['description']
        selected_category = request.POST['selected_subcategory']
        body = request.POST['body']
        if title == '' or description == '' or selected_category == '' or body == '':
            error_messages.append('All Fields Required.')

        if len(request.FILES) > 0:
            image = request.FILES['image']
            if not str(image.content_type).startswith('image'):
                error_messages.append('Your File Type Not Supported, Choose An Image.')
            else:
                if image.size > 4000000:
                    error_messages.append('Your Image Must Be Smaller Than 4 MB.')

        if len(error_messages) > 0:
            return render(
                request, 'back/edit_news.html',
                {'errors': error_messages, 'subcategories': subcategories, 'news': news}
            )
        if image:
            if os.path.exists(news.image.path):
                os.remove(news.image.path)

        news.__dict__.update(
            {
                'title': title,
                'description': description,
                'body': body,
                'image': image if image else news.image,
                'subcategory_id': selected_category
            }
        )
        news.save()
        return redirect('news:list')
    return render(request, 'back/edit_news.html', {'news': news, 'subcategories': subcategories})
