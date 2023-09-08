from rest_framework import serializers
from datetime import datetime, date

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(help_text="Имя пользователя (2)")
    password = serializers.CharField(help_text="Пароль пользователя (2)")

class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(help_text="Имя пользователя (2)")
    password = serializers.CharField(help_text="Пароль пользователя (2)")
    confirm = serializers.CharField(help_text="Подтверждение пароля (2)")