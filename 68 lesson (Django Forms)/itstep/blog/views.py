from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Post, Tag, Rating
from .forms import TagForm, TagFormModel, RatingForm


@login_required
def rate_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            score = form.cleaned_data['score']
            rating, created = Rating.objects.update_or_create(
                post=post,
                user=user,
                defaults={'rating': score}
            )
            mess_value = "created" if created else "updated"
            messages.success(request, f"Rating for {post.title} with score {rating.rating} was {mess_value}")
            return redirect(reverse('blog:post-detail', kwargs={'id': post_id}))
        else:
            messages.error(request, form.errors)
    else:
        form = RatingForm()

    return render(request, 'blog/post/detail.html', {'post': post, 'form': form})


def post_list(request):
    posts = Post.objects.all()
    return render(request, template_name="blog/post/list.html", context={'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    avg_rating = post.ratings.aggregate(Avg('rating'))['rating__avg'] or 0
    ratings = post.ratings.select_related('user')
    star_range = [i for i in range(5, 0, -1)]
    return render(request, 'blog/post/detail.html', {
        'post': post,
        'avg_rating': avg_rating,
        'ratings': ratings,
        'star_range': star_range,
        'form': RatingForm()
    })


def post_cards(request):
    posts = Post.objects.all()
    return render(request, template_name="index.html", context={'posts': posts})


def create_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            tag = Tag.objects.create(**form.cleaned_data)
            messages.success(request, f"Tag {tag.slug} was created!")
            return redirect('blog:create-tag')
        else:
            messages.error(request, 'Please correct the error below.')
            return render(request, template_name="blog/tag/create_tag.html", context={"form": form})
    form = TagForm()
    tags = Tag.objects.all()
    return render(request, template_name="blog/tag/create_tag.html", context={"form": form, "tags": tags})


def edit_tag(request, pk=None):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        form = TagFormModel(data=request.POST, instance=tag)
        if form.is_valid():
            updated_tag = form.save()
            messages.success(request, f'Tag "{updated_tag.name}" was updated.')
            return redirect("blog:create-tag")
        else:
            tags = []
            return render(request, 'blog/tag/edit_tag.html', {'form': form, "tags": tags})
    else:
        form = TagFormModel(instance=tag)
        tags = Tag.objects.all()
        return render(request, 'blog/tag/edit_tag.html', {'form': form, "tags": tags})


def delete_tag(request, pk=None):
    tag = get_object_or_404(Tag, pk=pk)
    tag.delete()
    messages.success(request, f'Tag "{tag.name}" was deleted')
    # delete() returns how many objects were deleted and how many
    # deletions were executed by object type: (1, {'blog.Tag': 1})
    return redirect("blog:create-tag")
