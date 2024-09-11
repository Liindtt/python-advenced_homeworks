from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from .forms import TagForm, TagFormModel


def post_list(request):
    posts = Post.objects.all()
    return render(request, template_name="blog/post/list.html", context={'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post/detail.html', {'post': post})


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
