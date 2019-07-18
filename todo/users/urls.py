from django.urls import path
from users import views

#from users.views import UserViewSet
#from rest_framework.routers import DefaultRouter
#router = DefaultRouter()
#router.register(r'users', UserViewSet, basename='user')
#urlpatterns = router.urls

urlpatterns = [
    path('', views.UserList.as_view(), name='user-list'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]