from django.urls import path, include
from users import views
from users.views import UserViewSet
from rest_framework.routers import DefaultRouter

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
    path('', include(router.urls)),
]