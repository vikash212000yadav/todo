from django.urls import path, include
from todos import views
from todos.views import TodoViewSet
from rest_framework.routers import DefaultRouter
from todos.views import waiting_to_working, working_to_complete

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
    path('', include(router.urls)),
    #path('', include('rest_auth.urls')),
    path('<int:id>/start', waiting_to_working),
    path('<int:id>/complete', working_to_complete),
)
