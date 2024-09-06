from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Department(models.Model):
    HR = 'HR'
    SALES = 'Sales'
    DEPARTMENT_CHOICES = [
        (HR, 'HR'),
        (SALES, 'Sales'),
    ]

    name = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    company = models.ForeignKey(Company, related_name='departments', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.company.name}"


class CustomUser(AbstractUser):
    STANDARD_USER = 'Standard'
    SUPER_USER = 'SuperUser'
    ROLE_CHOICES = [
        (STANDARD_USER, 'Standard User'),
        (SUPER_USER, 'Super User'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    department = models.ForeignKey(Department, related_name="users", on_delete=models.CASCADE, null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',  # Custom related_name for groups
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  # Custom related_name for user_permissions
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return f"{self.username} ({self.role})"


class upload(models.Model):
    name = models.CharField(max_length=224, blank=True)
    rdoc = models.FileField(upload_to='rdocs/', blank=True)
