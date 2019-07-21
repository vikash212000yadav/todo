from django.urls import path, include
from users import views
from users.views import UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import renderers

router = DefaultRouter()
router.register('', views.UserViewSet)

user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    #path('', views.UserList.as_view(), name='user-list'),
    #path('', user_list, name='user-list'),
    path('', include(router.urls)),
    #path('<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    #path('<int:pk>/', user_detail, name='user-detail'),
]