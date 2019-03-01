from django.db import models

# Create your models here.

# below are copyed from the board project
from django.contrib.auth.models import User

from django.core.validators import MinLengthValidator

'''
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)



class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics')
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
'''

class Item(models.Model):
    # warehousenum = models.IntegerField(unique = True)
    warehousenum = models.CharField(validators=[MinLengthValidator(10)], max_length = 10, blank = False)
    # invoicenum = models.IntegerField()
    invoicenum = models.CharField(validators=[MinLengthValidator(10)], max_length = 10, blank = False)
    MANUFACTURER = (
    ('Apple', 'Apple'),
    ('Dell', 'Dell'),
    ('HP', 'HP'),
    ('MicroSoft', 'MicroSoft'),
    ('Lenovo', 'Lenovo'),
    ('Google', 'Google'),
    # ('')
    )
    manufacturer = models.CharField(max_length = 300, choices = MANUFACTURER)
    ITEM_TYPE = (
    ('Laptop', 'Laptop'),
    ('Desktop', 'Desktop'),
    ('Printer', 'Printer'),
    ('HardDrive', 'HardDrive'),
    # ('')
    )
    item_type = models.CharField(max_length = 200, choices = ITEM_TYPE)
    recieved_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.warehousenum
class Donor(models.Model):
    # this should be a one-to-many field (i think), have no idea if it's possible...
    donorname = models.CharField(max_length = 200)
    donor_email = models.CharField(max_length = 1000)
    # donor_phone = models.IntegerField(unique = True)
    donor_phone = models.CharField(max_length = 100)
    donor_address = models.CharField(max_length = 2000)
    last_updated = models.DateTimeField(auto_now_add = True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name = 'donors')
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'donors')

class Type(models.Model):
    type_of_item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name = 'types')
    model_of_item = models.CharField(max_length = 1000)
    attribute_name = models.CharField(max_length = 2000)

class Test(models.Model):
    POWER_TEST = (
        ('Y', 'Pass.'),
        ('N', 'Fail.')
    )
    power_test = models.CharField(max_length = 100, choices = POWER_TEST)
    tested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'tests')

class Evaluation(models.Model):
    evaluation_stage = models.ForeignKey(Item, on_delete=models.CASCADE, related_name = 'evaluation')
    evaluated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'evaluation')
    evaluated_at = models.DateTimeField(auto_now_add = True)
