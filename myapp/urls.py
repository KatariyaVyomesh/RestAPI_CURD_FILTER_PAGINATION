from django.urls import path
from . import views

urlpatterns = [
    path('blogpost/',views.BlogPostListCreate.as_view(),name='blogpost-view-create'),
    path('blogpost/<int:pk>/',views.BlogPostRetrieveUpdateDestroy.as_view(),name='update'),
    path('employee/',views.EmployeeListCreate.as_view(),name='employee-view-create'),
    path('employee/<int:pk>/',views.EmployeeRetrieveUpdateDestroy.as_view()),
    
]