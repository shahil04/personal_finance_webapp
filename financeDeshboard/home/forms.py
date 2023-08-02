from .models import *
from django import forms

from .models import *

class Income_add_form(forms.ModelForm):
    class Meta:
        model  = Income_add_model
        fields = '__all__'
        # fields = ["amount","account","catagory"] 
        # labels = {"amount":"amount","account":"account type","catagory":"catagory choose"}


class Expense_add_form(forms.ModelForm):
    class Meta:
        model  = Expanse_add_model
        fields = '__all__'

class Transfer_amount_form(forms.ModelForm):
    class Meta:
        model = Transfer_amount_model
        fields = '__all__'

class Budget_create_form(forms.ModelForm):
    class Meta:
        model  = Budget_create_model
        fields = '__all__'

class Goal_create_form(forms.ModelForm):
    class Meta:
        model  = Goal_create_model
        fields = '__all__'

class Daily_add_form(forms.ModelForm):
    class Meta:
        model = Daily_add_model
        fields = '__all__'