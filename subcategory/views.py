from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from . import models
from category.models import Category


@login_required()
def subcategories_list(request):
    subcategories = models.Subcategory.objects.all()
    return render(request, 'back/subcategories_list.html', {'subcategories': subcategories})


@login_required()
def add_subcategory(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        error_messages = []
        title = request.POST['title']
        category = request.POST['selected_category']
        if title == '' or category == '':
            error_messages.append('All Fields Required.')

        if len(error_messages) > 0:
            return render(request, 'back/add_subcategory.html', {'errors': error_messages, 'categories': categories})

        subcategory = models.Subcategory(title=title, category_id=int(category))
        subcategory.save()
        return redirect('subcategories_list')
    return render(request, 'back/add_subcategory.html', {'categories': categories})
