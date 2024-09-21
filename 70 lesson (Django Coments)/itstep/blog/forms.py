from django import forms
from .models import Tag, Post, Contact, Comment


class TagForm(forms.Form):
    name = forms.CharField(max_length=10, label="Title for tag", help_text="Enter your tag")
    slug = forms.SlugField(max_length=31)


class TagFormModel(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'slug']

    def clean_name(self):
        value = self.cleaned_data['name']
        return value.lower()

    def clean_slug(self):
        value = self.cleaned_data['slug']
        if len(value) < 3:
            raise forms.ValidationError("Length is lower then 3 symbols")
        return value

    def clean(self):
        cleaned_data = super().clean()
        if len(cleaned_data.get('name')) < 3:
            self.add_error(None, "idk")


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'status', 'category', 'tags', 'publish']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 5, 'cols': 40, 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'multiple': False}),
            'publish': forms.DateTimeInput(attrs={'type': 'datetime-local'})}
        labels = {'title': 'Назва публікації', 'body': 'Текст публікації'}


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')