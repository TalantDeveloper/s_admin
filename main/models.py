from datetime import datetime

from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Computer(models.Model):
    invention_id = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    years = models.DateField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.invention_id} {self.type} {self.years}"


class Department(models.Model):
    name = models.CharField(max_length=100)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    computer = models.ForeignKey(Computer, on_delete=models.SET_NULL, null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} {self.department} {self.computer}"

