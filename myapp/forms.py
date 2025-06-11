# Correct
from django import forms
from .models import ToDoList

class ToDoForm(forms.ModelForm):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    priority = forms.ChoiceField(choices=PRIORITY_CHOICES)
    status = forms.ChoiceField(choices=STATUS_CHOICES)
    class Meta:
        model = ToDoList
        fields = '__all__' 
