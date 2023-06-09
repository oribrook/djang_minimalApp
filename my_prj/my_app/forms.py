from django import forms
from .models import Car
from django.core.validators import (RegexValidator, 
                                    EmailValidator,
                                    URLValidator,
                                    MaxValueValidator,
                                    )

from django.core.exceptions import ValidationError


class CarForm(forms.ModelForm):
    year = forms.IntegerField(validators=[MaxValueValidator(limit_value=2024)])
    email = forms.EmailField(required=False, label='הודעת אישור תגיע למייל במידה ותציין')
    class Meta:        
        model = Car
        fields = '__all__'
        # exclude = ['owner']


class DatePicker(forms.TextInput):
    input_type = 'date'
    

def my_validator(number):    
    if number % 2 != 0:
        raise ValidationError('Number is not even')


class ContactForm(forms.Form):
    img = forms.FileField(required=False)        
    name = forms.CharField(validators=[RegexValidator("[a-zA-Z ]"),])
    number = forms.IntegerField(validators=[my_validator], required=False)    
    city = forms.ChoiceField(choices=[
        ('jer', 'ירושלים'),
        ('tlv', 'תל אביב'),
        ('bs', 'באר שבע'),
    ], initial='tlv')    
    date = forms.DateField(widget=DatePicker(), required=False)
    car = forms.ModelChoiceField(queryset=Car.objects.all(), required=False)

    error_css_class = 'my_error_class'
