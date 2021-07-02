from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


def index(request):
    queryset = Post.objects.all().order_by('date')
    paginator = Paginator(queryset, 2)
    page_number = request.GET.get('page')
    try:
        data = paginator.get_page(page_number)
    except PageNotAnInteger:
        data = paginator.get_page(1)
    except EmptyPage:
        data = paginator.get_page(1)
    context = {
        'queryset': queryset,
        'data': data,
    }
    return render(request, 'index.html', context)


def blog(request, blog_id):
    blog = get_object_or_404(Post, id=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'blog.html', context)
