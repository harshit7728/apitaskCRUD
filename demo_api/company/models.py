from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['Company_data']


from django.conf import settings

# MongoDB collections
db = settings.MONGO_DB

class Department:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def create_department(name):
        department = {
            'name': name,
            'users': []
        }
        db.departments.insert_one(department)
        return department

    @staticmethod
    def get_department(name):
        return db.departments.find_one({'name': name})

class User:
    def __init__(self, username, email, department, role):
        self.username = username
        self.email = email
        self.department = department  # Either 'HR' or 'Sales'
        self.role = role  # Either 'Standard User' or 'Super User'

    @staticmethod
    def create_user(username, email, department, role):
        user = {
            'username': username,
            'email': email,
            'department': department,
            'role': role,
        }
        db.users.insert_one(user)
        db.departments.update_one(
            {'name': department},
            {'$push': {'users': user}}
        )
        return user

    @staticmethod
    def get_users_by_department(department):
        return list(db.users.find({'department': department}))


# class Company(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
#
#
# class Department(models.Model):
#     HR = 'HR'
#     SALES = 'Sales'
#     DEPARTMENT_CHOICES = [
#         (HR, 'HR'),
#         (SALES, 'Sales'),
#     ]
#
#     name = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
#     company = models.ForeignKey(Company, related_name='departments', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.name} - {self.company.name}"
#
#
# class CustomUser(AbstractUser):
#     STANDARD_USER = 'Standard'
#     SUPER_USER = 'SuperUser'
#     ROLE_CHOICES = [
#         (STANDARD_USER, 'Standard User'),
#         (SUPER_USER, 'Super User'),
#     ]
#
#     role = models.CharField(max_length=20, choices=ROLE_CHOICES)
#     department = models.ForeignKey(Department, related_name="users", on_delete=models.CASCADE, null=True, blank=True)
#
#     groups = models.ManyToManyField(
#         Group,
#         related_name='customuser_groups',
#         blank=True,
#         help_text='The groups this user belongs to.',
#         verbose_name='groups',
#     )
#
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name='customuser_permissions',
#         blank=True,
#         help_text='Specific permissions for this user.',
#         verbose_name='user permissions',
#     )
#
#     def __str__(self):
#         return f"{self.username} ({self.role})"
#
#
# class upload(models.Model):
#     name = models.CharField(max_length=224, blank=True)
#     rdoc = models.FileField(upload_to='rdocs/', blank=True)
