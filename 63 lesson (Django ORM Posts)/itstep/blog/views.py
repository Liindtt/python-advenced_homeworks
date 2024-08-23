from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Post, Rating


def post_list(request):
    publish_param = request.GET.get('publish')
    print(publish_param)
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
