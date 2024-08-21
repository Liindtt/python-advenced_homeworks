from django.shortcuts import render, get_object_or_404
from .models import Post, Tag


def post_list(request):
    posts = Post.objects.all()
    return render(request, template_name="blog/post/list.html", context={'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post/detail.html', {'post': post})


def post_cards(request):
    posts = Post.objects.all()
    return render(request, template_name="index.html", context={'posts': posts})


def post_by_tag(request, slug):
    tag_name = get_object_or_404(Tag, slug=slug).name
    posts = Post.objects.filter(tags__slug=slug)
    return render(request, 'blog/post/posts_by_tag.html', {'posts': posts, 'tag_name': tag_name})
