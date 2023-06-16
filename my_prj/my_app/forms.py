from django import forms
from .models import Car
from django.core.validators import (RegexValidator, 
                                    EmailValidator,
                                    URLValidator,
                                    MaxValueValidator,
                                    )

from django.core.exceptions import ValidationError


class CarForm(forms.ModelForm):
    # year = forms.IntegerField(validators=[MaxValueValidator(limit_value=2024, message="Year error")])

    # def __init__(self, is_year_editable=True, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['year'].disabled = not is_year_editable

    class Meta:
        model = Car
        fields = '__all__'
        # exclude = ['owner']


        labels = {
            "car_type": 'enter car model',
            "year": "enter car year",
        }

        error_messages = {
            "year": {
                "required": "השדה הזה הוא חובה",
            }
        }


class DatePicker(forms.TextInput):
    input_type = 'date'
    

def my_validator(number):    
    if number % 2 != 0:
        raise ValidationError('Number is not even')


class ContactForm(forms.Form):
    img = forms.FileField(required=False, label="add image")
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


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
