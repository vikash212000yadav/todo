from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from todos import views

urlpatterns = (
    path('', views.TodoList.as_view(), name='todo-list'),
    path('<int:pk>/', views.TodoDetail.as_view(), name='todo-detail'),
    path('<int:pk>/start', views.Status_start.as_view(), name = 'status'),
    path('<int:pk>/complete', views.Status_complete.as_view(), name = 'status'),
    #path('<int:pk>/complete', views.Status.as_view(), name = 'status'),

)
