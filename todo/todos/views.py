from todos.models import Todo
from rest_framework import permissions
from todos.serializers import TodoSerializer
from todos.permissions import IsUserOrReadOnly
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsUserOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(['GET', 'POST'])
def waiting_to_working(request, id):
    todo = Todo.objects.get(id=id)
    if todo.status == 'WA':
        todo.status = 'WR'
        todo.save()
        return Response('', status=status.HTTP_200_OK)
    else:
        Todo_serializer = TodoSerializer(todo, data=request.data)
        if Todo_serializer.is_valid():
            Todo_serializer.save()
            return Response({"data": 'ID Updated successfully.'}, status=status.HTTP_200_OK)
        else:
            error_details = []
            for key in Todo_serializer.errors.keys():
                error_details.append({"field": key, "message": Todo_serializer.errors[key][0]})
            data = {
                "Error": {
                    "status": 400,
                    "message": "Your submitted data was not valid - please correct the below errors",
                    "error_details": error_details
                }
            }

    return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def working_to_complete(request, id):
    todo =Todo.objects.get(id=id)
    if todo.status == 'WR':
        todo.status = 'DN'
        todo.save()
        return Response('', status=status.HTTP_200_OK)
    else:
        Todo_serializer = TodoSerializer(todo, data=request.data)
        if Todo_serializer.is_valid():
            Todo_serializer.save()
            return Response({"data": 'ID Updated successfully.'}, status=status.HTTP_200_OK)
        else:
            error_details = []
            for key in Todo_serializer.errors.keys():
                error_details.append({"field": key, "message": Todo_serializer.errors[key][0]})
            data = {
                "Error": {
                    "status": 400,
                    "message": "Your submitted data was not valid - please correct the below errors",
                    "error_details": error_details
                }
            }

    return Response(data, status=status.HTTP_400_BAD_REQUEST)


"""
def waiting_to_working(request, id=None):
    todo = Todo.objects.get(id=id)
    if todo.status == 'WA':
        todo.status = 'WR'
        todo.save()
    return todo"""