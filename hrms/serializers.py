from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . models import Department, Employee

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "name",
            "Email_Address",
            "zipcode",
            "Date_of_Birth",
            "password",

        ]

        extra_kwargs = {"password": {"write_only": True}}
        password = self.validated_data["password"]
        account.set_password(password)
        account.save()
        return account

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Department
        fields= ['id', 'name', 'history']

    def create(self, validted_data):
        return Department.objects.create(**validted_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.history = validated_data.get('history', instance.history)
        instance.save()
        return instance

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'emp_id', 'thumb', 'first_name', 'last_name', 'mobile', 'email', 'address', 'emergency', 'gender', 'department', 'joined', 'lamguage', 'bank', 'salary']

    def create(self, validted_data):
        return Employee.objects.create(**validted_data)

    def update(self, instance, validated_data):
        instance.emp_id = validated_data.get('name', instance.emp_id)
        instance.thumb = validated_data.get('thumb', instance.thumb)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.email = validated_data.get('email', instance.email)
        instance.address = validated_data.get('address', instance.address)
        instance.emergency = validated_data.get('emergency', instance.emergency)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.department = validated_data.get('department', instance.department)
        instance.joined = validated_data.get('joined', instance.joined)
        instance.language = validated_data.get('language', instance.language)
        instance.bank = validated_data.get('bank', instance.bank)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.save()
        return instance


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'url', 'username', 'email', 'groups']

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']