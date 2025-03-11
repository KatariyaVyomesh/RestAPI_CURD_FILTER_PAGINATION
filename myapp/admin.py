from django.contrib import admin
from .models import BlogPost
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display=('title','content','published_date')
admin.site.register(BlogPost,BlogPostAdmin)

from .models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'position', 'department','hire_date','salary')
admin.site.register(Employee,EmployeeAdmin)