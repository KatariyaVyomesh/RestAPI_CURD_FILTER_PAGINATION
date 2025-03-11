import django_filters 
from .models import Employee
class EmployeeFilter(django_filters.FilterSet):
    salary = django_filters.RangeFilter()  # Allows filtering salaries within a range

    class Meta:
        model = Employee
        fields = ['department', 'position', 'first_name', 'salary']
