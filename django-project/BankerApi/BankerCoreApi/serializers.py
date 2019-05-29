from .models import Manager, Users, Organization
from rest_framework import serializers


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ("UserID", "UserIDEncrypted", "PasswordBase64", "EncryptedPasswordEncoded", "LoginEmail", "FirstName", "LastName", "Address", "Address2", "City", "ZipCode", "PhoneNumber")
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ("title", "artist")
class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ("OrganizationID", "OrganizationName", "OrganizationNameLowercase", "ZipCode", "DateCreated", "DateVerified", "IsActive", "IsCreatorVerified", "CreatorEmail", "CreatorWebID")