from django import forms
from django.core.validators import URLValidator
from .models import Car
import datetime

class MyForm(forms.Form):

    last_name = forms.CharField()
    first_name = forms.CharField(required=False)
    age = forms.IntegerField(widget=forms.TextInput(attrs={'style': 'color: red'}))
    
    start_date = forms.DateField(initial=datetime.datetime.now())    
    end_date = forms.DateField(widget=forms.SelectDateWidget())
    # end_date = forms.DateField(forms.SelectDateWidget(years=range(1950, 2024)))
    
    email = forms.EmailField(required=True, initial="ori@logicode.study")

    city = forms.ChoiceField(choices=[('JR', "Jerusalem"),
                                    ('TLV', "Tel-Aviv"),
                                    ('BS', "Be'er-Sheva")])
    car = forms.ModelChoiceField(queryset=Car.objects.all())
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': '15'}), max_length=500)
    
    agree = forms.BooleanField(label="Accept terms of use")

    site = forms.CharField(validators=[URLValidator()])