from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=get_user_model().objects.all())])
    password = serializers.CharField(write_only='true')
    re_password = serializers.CharField(write_only='true')
    is_superuser = serializers.IntegerField(read_only='true')
    is_staff = serializers.IntegerField(read_only='true')
    is_active = serializers.IntegerField(read_only='true')
    last_login = serializers.DateTimeField(read_only='true')
    date_joined = serializers.DateTimeField(read_only='true')

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = (
        'id', 'username', 'email', 'password', 're_password',
        'is_superuser', 'is_staff', 'is_active', 'last_login',
        'date_joined')