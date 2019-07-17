from django.urls import path
#from rest_framework.urlpatterns import format_suffix_patterns
from todos import views

urlpatterns = [
    path('todos/', views.TodoList.as_view(), name='todo-list'),
    path('todos/<pk>/', views.TodoDetail.as_view(), name='todo-detail'),
]