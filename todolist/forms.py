from django import forms
from .models import TodoList



class UserCreationForm(forms.ModelForm):
  
    

    class Meta:
        model = TodoList
        fields = ('title', 'description')




class UserChangeForm(forms.ModelForm):
    
    class Meta:
        model = TodoList
        fields = ('title', 'description')
        