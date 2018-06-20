from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only='true')
    re_password = serializers.CharField(write_only='true')

    def create(self, validated_data):
        user = get_user_model().objects.create(
            email = validated_data['email']
        )
        if password == re_password:
            user.set_password(validated_data['password'])
            user.save()
            return user

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 're_password')