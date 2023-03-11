from django import forms
from .models import Search


class SearchForm(forms.ModelForm):
    address = forms.CharField(label='')
    # class Meta defines how the forms behave or how forms should look like
    class Meta:
        model = Search
        fields = ['address',]