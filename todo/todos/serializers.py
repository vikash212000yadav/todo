from rest_framework import serializers
from todos.models import Todo

class TodoSerializer(serializers.Serializer):
    class Meta:
        model = Todo
        fields = '__all__'

        extra_kwargs = {
                'url': {
                    'view_name': 'todos:todo-detail',                    
                }                
        }
