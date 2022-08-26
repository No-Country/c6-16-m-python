from tkinter import CASCADE
from django.db import models
from users.models import User
from reserves.models import Reserve
from enum import Enum
# Create your models here.

class OrderStatus(Enum):
    CREATED = 'CREATED'
    PAYED = 'PAYED'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'

choices = [ (tag, tag.value) for tag in OrderStatus ]

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reserve = models.ForeignKey(Reserve, on_delete=models.CASCADE)
    status = models.CharField(max_length=40, choices=choices, default=OrderStatus.CREATED) 
    total = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ''

