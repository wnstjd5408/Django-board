from django import forms
from django.forms import fields, widgets
from bo.models import Board


class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ['title', 'comment']
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }
