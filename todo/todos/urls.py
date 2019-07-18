from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from todos import views

urlpatterns = (
    path('', views.TodoList.as_view(), name='todo-list'),
    path('<int:pk>/', views.TodoDetail.as_view(), name='todo-detail'),
    #path('<int:pk>/start', views.TodoDetail.as_view(), name = 'todo-detail')
)
