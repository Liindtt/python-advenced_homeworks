from django import forms
from .models import Tag, Rating


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


class RatingForm(forms.Form):
    RATING_CHOICES = [(i, str(i)) for i in range(5, 0, -1)]
    score = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio_1'}),
                              label="Score")


