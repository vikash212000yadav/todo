from todos.models import Todo, Status
from rest_framework import generics
from rest_framework import permissions
from todos.serializers import TodoSerializer
from todos.permissions import IsUserOrReadOnly
from rest_framework.views import APIView

class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class Status_start(generics.ListCreateAPIView):
    #queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        #user = self.request.user
        return Todo.objects.filter(choice='Working')

class Status_complete(generics.ListCreateAPIView):
    #queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        #user = self.request.user
        return Todo.objects.filter(choice='Complete')
