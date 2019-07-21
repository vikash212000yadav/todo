from django.urls import path, include
# from rest_framework.urlpatterns import format_suffix_patterns
from todos import views
from todos.views import TodoViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import renderers

router = DefaultRouter()
router.register('', views.TodoViewSet)

todo_list = TodoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
todo_detail = TodoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = (
    #path('', views.TodoList.as_view(), name='todo-list'),
    #path('', todo_list, name='todo-list'),
    path('', include(router.urls)),
    #path('<int:pk>/', views.TodoDetail.as_view(), name='todo-detail'),
    #path('<int:pk>/', todo_detail, name='todo-detail'),
    path('<int:pk>/start', views.Status_start.as_view(), name = 'status'),
    path('<int:pk>/complete', views.Status_complete.as_view(), name = 'status'),
    #path('<int:pk>/complete', views.Status.as_view(), name = 'status'),

)
