from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db.models import Q
from .models import Post, Rating, Category


def post_list(request):
    publish_param = request.GET.get('publish')
    if publish_param == 'published':
        posts = Post.published.get_queryset()
        return render(request, template_name="blog/post/list.html", context={'posts': posts})

    posts = Post.objects.all()
    return render(request, template_name="blog/post/list.html", context={'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    ratings = get_list_or_404(Rating, post=post)

    avg_rating = round(sum(r.rating for r in ratings) / len(ratings), 1)
    return render(request, 'blog/post/detail.html', {'post': post, 'range': range(1, 6),
                                                     'ratings': ratings, 'avg_rating': avg_rating})


def search_posts(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query),
            status=Post.Status.PUBLISHED
        ).distinct()
    else:
        posts = Post.objects.all()

    categories = Category.objects.all()

    return render(request, 'blog/post/list.html', {'posts': posts, 'query': query, 'categories': categories})


def posts_by_category(request, category_id=None):
    categories = Category.objects.all()
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        posts = Post.objects.filter(category=category, status=Post.Status.PUBLISHED)
        category_name = category.title
    else:
        posts = Post.published.all()
        category_name = "All Categories"

    return render(request, 'blog/post/posts_by_category.html', {'posts': posts, 'category_name': category_name, 'categories': categories})
