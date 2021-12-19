from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Person 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Group, 
        fields = ['url', 'name']

class PersonSerializer(serializers.Serializer):
    firstName = serializers.CharField(max_length=128)
    lastName = serializers.CharField(max_length=128)
    phone = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=256)
    postcode = serializers.CharField(max_length=8)
    
    def create(self, validated_data):
        return Person.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.lastName = validated_data.get('lastName', instance.lastname)
        instance.save()
        return instance