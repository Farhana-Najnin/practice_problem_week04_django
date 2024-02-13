from django import forms
from django.forms.widgets import NumberInput
import datetime
from first_app.models import PracticeModel

YEAR_CHOICES =  ['1960','1970','1980', '1990', '2000']
TOPIC_CHOICES = [
    ('topic1','Topic1'),
    ('topic2','Topic2'),
    ('topic3','Topic3'),
    ('topic4','Topic4'),
]
class contact_form(forms.Form):
    first_name = forms.CharField()
    name = forms.CharField(label="Enter your Name", required=True)
    email = forms.EmailField(required=True, label="Enter your email")
    roll = forms.IntegerField(help_text='Give 5 digit roll')
    date = forms.DateField(required=False)
    BirthDate = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    BirthYear = forms.DateField(widget=forms.SelectDateWidget(years=YEAR_CHOICES))
    value = forms.DecimalField()
    day = forms.DateField(initial= datetime.date.today)
    favorite_color = forms.ChoiceField(choices=TOPIC_CHOICES)

    topic = forms.ChoiceField(widget=forms.RadioSelect,choices=TOPIC_CHOICES)

    favoriteTopic = forms.MultipleChoiceField(choices=TOPIC_CHOICES) 

    MultipleTopicChoice= forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=TOPIC_CHOICES)
    comment = forms.CharField(min_length=50,required=False,initial='comment here...',widget = forms.Textarea(attrs={'rows' : 4}))
    file = forms.FileField()
    message = forms.CharField(min_length= 20, max_length=40)
    Agree = forms.BooleanField(required=False, initial=True)
   
class PracticeForm(forms.ModelForm):
    class Meta:
        model = PracticeModel
        fields = '__all__'