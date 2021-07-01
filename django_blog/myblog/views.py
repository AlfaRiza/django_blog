from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.

def index(request):
    queryset = Post.objects.all()
    context = {
        'queryset': queryset,
    }
    return render(request, 'index.html', context)


def blog(request):
    # blog = get_object_or_404(Post, id = blog_id)
    return render(request, 'blog.html')
