from django import forms

from todoapp.models import Todo


class Todo_Form(forms.ModelForm):
            class Meta:
                          model = Todo
                          fields = ['task','priority','date']