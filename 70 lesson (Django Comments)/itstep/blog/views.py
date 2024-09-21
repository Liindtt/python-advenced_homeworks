from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag, Comment
from .forms import TagFormModel, PostForm, ContactForm, CommentForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, template_name="blog/post/list.html", context={'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            messages.success(request, "Your comment has been added.")
        else:
            messages.error(request, "Please correct error below.")
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html', {'post': post, 'comments': comments,
                                                     'new_comment': new_comment, 'comment_form': comment_form})


def post_cards(request):
    posts = Post.objects.all()
    return render(request, template_name="index.html", context={'posts': posts})


def create_tag(request):
    form = TagFormModel(request.POST or None)
    if form.is_valid():
        tag = form.save()
        messages.success(request, f"Tag {tag.slug} was created!")
        return redirect('blog:edit-tag')
    elif request.method == "POST":
        messages.error(request, 'Please correct the error below.')
        return render(request, template_name="blog/tag/create_tag.html", context={"form": form})

    tags = Tag.objects.all()
    return render(request, template_name="blog/tag/create_tag.html", context={"form": form, "tags": tags})


def edit_tag(request, pk=None):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method=="POST":
        form = TagFormModel(data=request.POST, instance=tag)
        if form.is_valid():
            updated_tag = form.save()
            messages.success(request, 'Tag "{}" was updated.'.format(updated_tag.slug))
            return redirect("blog:edit-tag", tag.pk)
        tags = []
        return render(request, 'blog/tag/create_tag.html', {'form': form, "tags": tags})
    form = TagFormModel(instance=tag)
    tags = Tag.objects.all()
    return render(request, 'blog/tag/create_tag.html', {'form': form, "tags": tags})


def delete_tag(request, pk=None):
    tag = get_object_or_404(Tag, pk=pk)
    tag.delete()
    messages.success(request, f"Tag {tag.slug} was deleted")
    # delete() returns how many objects were deleted and how many
    # deletions were executed by object type: (1, {'blog.Tag': 1})
    return redirect("blog:create-tag")


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            messages.success(request, f"Post {new_post.title} was created")
            return redirect('blog:post-detail', new_post.pk)
        else:
            messages.success(request, f"Please correct the error below.")
            return render(request, 'blog/post/create_post.html', {'form': form})

    form = PostForm()
    return render(request, 'blog/post/create_post.html', {"form": form})


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            updated_post = form.save()
            messages.success(request, f"Post {updated_post.title} was updated!")
            return redirect('blog:post-detail', updated_post.pk)
        else:
            messages.success(request, f"Please correct the error below.")
            return render(request, 'blog/post/edit_post.html', {'form': form})
    form = PostForm(instance=post)
    return render(request, 'blog/post/edit_post.html', {"form": form})


def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, f'Post "{post.title}" was deleted.')
        return redirect('blog:post-list')
    return render(request, 'blog/post/detail.html', {'post': post})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('blog:contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form})
