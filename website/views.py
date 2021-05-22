from django.shortcuts import render

from website.models import Post, Category, Tag


def index(request):
    context = {
        'posts': Post.objects.all().order_by('created_at'),
        'odd_categories': Category.objects.all().order_by('name')[::2],
        'even_categories': Category.objects.all().order_by('name')[1::2],
        'odd_tags': Tag.objects.all().order_by('name')[::2],
        'even_tags': Tag.objects.all().order_by('name')[1::2]
    }
    return render(request, 'blog/index.html', context=context)


def details(request, pk=None):
    context = {
        'post': Post.objects.get(pk=pk) if pk is not None else None,
        'category': Post.objects.get(pk=pk).category,
        'odd_tags': Post.objects.get(pk=pk).tags.order_by('name')[::2],
        'even_tags': Post.objects.get(pk=pk).tags.order_by('name')[1::2]
    }
    return render(request, 'blog/post.html', context=context)


def create(request):
    context = {}
    return render(request, 'blog/create.html', context=context)
