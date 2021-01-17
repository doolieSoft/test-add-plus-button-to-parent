from django import forms
from .models import Child, Parent

class ChildForm(forms.ModelForm):
    class Meta:
        model=Child
        fields = '__all__'


class ParentForm(forms.ModelForm):
    class Meta:
        model=Parent
        fields = '__all__'