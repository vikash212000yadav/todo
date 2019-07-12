from rest_framework import serializers
from todos.models import Todo

class TodoSerializer(serializers.HyperlinkedModeSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

        extra_kwargs = {
                'url': {
                    'view_name': 'todos:todo-detail',                    
                }                
        }
