from django.contrib import admin
from .models import Todo
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    class Meta:
        model = Todo
admin.site.register(Todo,TodoAdmin)




