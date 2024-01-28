from django.contrib.auth.hashers import make_password
from .models import LibararyUser
from rest_framework import serializers



class LibararyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibararyUser
        fields = '__all__'



