from users.models import User
from rest_framework import generics
#from rest_framework import permissions
#from users.permissions import IsUserOrReadOnly
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsUserOrReadOnly]

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)
