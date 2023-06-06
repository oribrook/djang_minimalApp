from django import forms
from .models import Car


class DatePicker(forms.TextInput):
    input_type = 'date'
    

class ContactForm(forms.Form):

    car_type = forms.CharField(required=False, 
            widget=forms.TextInput(attrs={'style': 'color: red;'}))

    date3 = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'date'}))

    min_cost = forms.FloatField(min_value=0, required=False, 
        widget=forms.NumberInput(attrs={'class': 'myclass'}))


    max_cost = forms.FloatField(min_value=0, required=False)
    first_hand = forms.BooleanField(required=False)
    terms = forms.BooleanField(required=True, label="האם אתה מסכים לתנאי השירות")

    city = forms.ChoiceField(choices=[
        ('jer', 'ירושלים'),
        ('tlv', 'תל אביב'),
        ('bs', 'באר שבע'),
    ], initial='tlv')

    car = forms.ModelChoiceField(queryset=Car.objects.all())

    date = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2040)))
    date1 = forms.DateField(widget=forms.SelectDateWidget(years=[1,2,3]))
    date2 = forms.DateField(widget=DatePicker())


    lname = forms.CharField(widget=forms.Textarea(attrs={'rows': "3"}))
