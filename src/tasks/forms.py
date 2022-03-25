from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
   
    task = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'border-indigo-900 border-2 rounded-3xl shadow-md focus:indigo-600 w-96  placeholder-indigo-500::placeholder',
        'placeholder': 'Enter your task'}))
      

    def clean_task(self):
        task = self.cleaned_data.get("task")
        # query set to filter and check if it exists or not
        task_qs = Todo.objects.filter(task=task)
        if task_qs.exists():
            # checks if at all such a task doesnt exist in the database
            raise forms.ValidationError("Task Already Exists!")
        return task

    class Meta:
        model = Todo
        fields=['task']    

    






