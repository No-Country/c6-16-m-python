from operator import truediv
from pyexpat import model
from django.db import models
from users.models import User
from parking.models import Parking
import uuid
# Create your models here.

from django.db.models.signals import pre_save
class Reserve(models.Model):
    reserve_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    parkings = models.ManyToManyField(Parking)
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.parkings} con id:{self.reserve_id}' 

def set_reserve_id(sender, instance, *args, **kwargs):
    if not instance.reserve_id:
        instance.reserve_id = str(uuid.uuid4())
        
pre_save.connect(set_reserve_id, sender=Reserve)
