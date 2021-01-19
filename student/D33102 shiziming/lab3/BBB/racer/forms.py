from django import forms
from .models import group,Racer,Racing_car

class racerForm(forms.ModelForm):
    class Meta:
        model = Racer
        fields = ('racer_name','Introduction','rank','ID_group')

class groupForm(forms.ModelForm):
    class Meta:
        model = group
        fields = ('Group_name',)