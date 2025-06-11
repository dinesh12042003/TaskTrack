from django.contrib import admin
from .models import ToDoList

# Display all fields in the admin list view
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('task', 'task_desc', 'priority', 'assigned_on', 'deadline', 'status')
    list_filter = ('priority', 'status', 'assigned_on', 'deadline')  # Optional filters
    search_fields = ('task', 'task_desc', 'priority', 'status')      # Search bar in admin

admin.site.register(ToDoList, ToDoListAdmin)
