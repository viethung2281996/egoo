from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        pass
    pass