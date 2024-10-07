from django.contrib.auth import get_user_model  #type:ignore
from rest_framework.serializers import ModelSerializer  #type:ignore

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id', 'username', 'first_name',
            'last_name', 'email'
        ]