from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Bounty

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class BountySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bounty
        # owner is read_only so users can't pass a fake owner ID in the JSON
        fields = ['id', 'target_name', 'reward', 'status', 'owner']
        read_only_fields = ['owner']