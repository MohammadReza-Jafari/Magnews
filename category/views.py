from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from . import models


@login_required()
def category_list(request):
    categories = models.Category.objects.all()
    return render(request, 'back/category_list.html', {'categories': categories})


@login_required()
def add_category(request):
    if request.method == 'POST':
        error_messages = []
        title = request.POST['title']
        if title == "":
            error_messages.append('All Fields Required')

        if models.Category.objects.filter(title__iexact=title):
            error_messages.append('This Category Added Before.')

        if len(error_messages) > 0:
            return render(request, 'back/add_category.html', {'errors': error_messages})

        category = models.Category(title=title)
        category.save()
        return redirect('category_list')
    return render(request, 'back/add_category.html')

