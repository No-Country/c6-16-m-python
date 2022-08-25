from pyexpat import model
from django.db import models
from users.models import User
from parking.models import Parking
import uuid
from django.db.models.signals import pre_save
from django.db.models.signals import m2m_changed

class Reserve(models.Model):
    reserve_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    parkings = models.ManyToManyField(Parking, through='ReserveParkings')
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.parkings} con id:{self.reserve_id}' 
    
    def update_totals(self):
        self.update_subtotal()
        self.update_total()
    
    def update_subtotal(self):
        self.subtotal = sum([parking.price_hour for parking in self.parkings.all() ])
        self.save()
    
    def update_total(self):
        FEE = 0.05
        self.total = self.subtotal + (self.subtotal * 1)
        self.save()

class ReserveParkings(models.Model):
    reserve = models.ForeignKey(Reserve, on_delete=models.CASCADE)
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)



def set_reserve_id(sender, instance, *args, **kwargs):
    if not instance.reserve_id:
        instance.reserve_id = str(uuid.uuid4())

def update_totals(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clean':
      instance.update_totals()

        
pre_save.connect(set_reserve_id, sender=Reserve)
# cuando se agregue una reserva, se elimine o se limpie se calculan los totales.
m2m_changed.connect(update_totals, sender=Reserve.parkings.through)
