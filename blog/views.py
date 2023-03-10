from django.shortcuts import render, get_object_or_404
from .models import AllBlogs


def all_blogs(request):
    blogs = AllBlogs.objects.order_by('-date')[:5]

    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/all_blogs.html', context)


def details(request, blog_id):
    blog = get_object_or_404(AllBlogs, pk=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/detail.html', context)
