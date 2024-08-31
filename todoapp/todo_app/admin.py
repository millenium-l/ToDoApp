from django.contrib import admin
from.models import Task, Author


class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "status"]
    list_filter = ('author', 'due_date')# used when filtering tasks
    search_fields = ["status", "title", "author"]

# Register your models here.
admin.site.register(Task, TaskAdmin)
admin.site.register(Author)

# custom Admin ui
admin.site.site_header = 'Tasker App'
admin.site.site_title = 'Taskers'