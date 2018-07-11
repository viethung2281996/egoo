from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only='true')
    re_password = serializers.CharField(write_only='true')

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username = validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = (
        'id', 'username', 'email', 'password', 're_password',
        'is_superuser', 'first_name', 'last_name', 'is_staff',
        'is_active', 'last_login', 'date_joined')