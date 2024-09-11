from django import forms
from .models import Tag


class TagForm(forms.Form):
    name = forms.CharField(max_length=10, label="Enter new tag")

    def save(self, instance, **kwargs):
        instance.update(**kwargs)
        instance.save()
        return instance


class TagFormModel(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
