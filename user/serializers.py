from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomInformation, Ticket
from rest_framework.validators import UniqueValidator

class CustomInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomInformation
        fields = (
            'avatar',
            )

class UserSerializer(serializers.ModelSerializer):
    custominformation = CustomInformationSerializer(read_only='true')
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
        if validated_data['re_password'] != validated_data['password']:
            error = {'message': 're_password and password not match'}
            raise serializers.ValidationError(error)
        user.set_password(validated_data['password'])
        user.save()
        custom_information = CustomInformation(user=user)
        custom_information.save()
        return user

    class Meta:
        model = get_user_model()
        fields = (
        'id', 'username', 'email', 'password', 're_password',
        'is_superuser', 'is_staff', 'is_active', 'last_login',
        'date_joined', 'custominformation')

class TicketSerializer(serializers.ModelSerializer):

    class Meta():
        model = Ticket
        fields = (
            'status',
            'start',
            'end',
            'category_id'
            )
