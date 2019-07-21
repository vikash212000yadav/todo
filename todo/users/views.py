from users.models import User
from rest_framework import generics
#from rest_framework import permissions
#from users.permissions import IsUserOrReadOnly
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework import renderers
from rest_framework import viewsets
User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    #@action(detail=True, renderer_class=[renderers.StaticHTMLRenderer])

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

"""class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsUserOrReadOnly]

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)
"""