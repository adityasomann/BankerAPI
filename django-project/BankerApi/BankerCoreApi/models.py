from django.db import models

# Create your models here.
class Users(models.Model):
    title = models.CharField(max_length=255, null=False)
    artist = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{0} - {1} " .format(self.title, self.artist)

class Manager(models.Model):
    UserID = models.CharField(max_length=255, null=False)
    UserIDEncrypted = models.CharField(max_length=255, null=False)
    PasswordBase64 = models.CharField(max_length=255, null=False)
    EncryptedPasswordEncoded = models.CharField(max_length=255, null=False)
    LoginEmail = models.CharField(max_length=255, null=False)
    FirstName = models.CharField(max_length=255, null=False)
    LastName = models.CharField(max_length=255, null=False)
    Address = models.CharField(max_length=255, null=False)
    Address2 = models.CharField(max_length=255, null=False)
    City = models.CharField(max_length=255, null=False)
    ZipCode = models.CharField(max_length=255, null=False)
    PhoneNumber = models.CharField(max_length=255, null=False)

class Organization(models.Model):
    OrganizationID = models.CharField(max_length =255, null = False)
    OrganizationName = models.CharField(max_length =255, null = False)
    OrganizationNameLowercase = models.CharField(max_length =255, null = False)
    ZipCode = models.CharField(max_length =255, null = False)
    DateCreated = models.CharField(max_length =255, null = False)
    DateVerified = models.CharField(max_length =255, null = False)
    IsActive = models.CharField(max_length =255, null = False)
    IsCreatorVerified = models.CharField(max_length =255, null = False)
    CreatorEmail = models.CharField(max_length =255, null = False)
    CreatorWebID = models.CharField(max_length =255, null = False)