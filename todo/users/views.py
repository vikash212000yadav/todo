from users.models import User
from users.serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import viewsets
User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
