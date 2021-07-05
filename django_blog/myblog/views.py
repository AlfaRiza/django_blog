from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .form import CommentForm, PostForm
from django.db.models import Q


# Create your views here.

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


def index(request):
    queryset = Post.objects.all().order_by('date')
    categories = Category.objects.all().order_by('id')
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
        'categories': categories,
    }
    return render(request, 'index.html', context)


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    categories = Category.objects.all().order_by('id')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
    paginator = Paginator(queryset, 2)
    page_number = request.GET.get('page')
    try:
        data = paginator.get_page(page_number)
    except PageNotAnInteger:
        data = paginator.get_page(1)
    except EmptyPage:
        data = paginator.get_page(1)
    context = {
        'data': data,
        'categories': categories,

    }
    return render(request, 'index.html', context)


def blog(request, blog_id):
    blog = get_object_or_404(Post, id=blog_id)
    categories = Category.objects.all()
    form = CommentForm(request.POST)
    # comment = Comment.objects.filter(post__id= blog_id)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = blog
            form.save()
            return redirect('blog', blog_id=blog_id)
    context = {
        'blog': blog,
        'categories': categories,
        'form': form,
        # 'comment': comment,
    }
    return render(request, 'blog.html', context)


def blog_create(request):
    title = 'Create Post'
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('blog', kwargs={
                'blog_id': form.instance.id
            }))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'post_create.html', context)


def blog_update(request, blog_id):
    title = 'Update Post'
    blog = get_object_or_404(Post, id=blog_id)
    form = PostForm(request.POST or None, request.FILES or None, instance=blog)
    author = get_author(request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('blog', kwargs={
                'blog_id': form.instance.id
            }))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'post_create.html', context)


def blog_delete(request, blog_id):
    blog = get_object_or_404(Post, id=blog_id)
    blog.delete()
    return redirect('index')


def categoryView(request, cats):
    category_post = Post.objects.filter(categories__title__contains=cats)
    categories = Category.objects.all()
    context = {
        'cats': cats,
        'category_post': category_post,
        'categories': categories,
    }
    return render(request, 'categories.html', context)
