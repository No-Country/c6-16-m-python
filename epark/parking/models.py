from django.db import models
from django.utils.text import slugify
import uuid
from django.db.models.signals import pre_save

# Create your models here.
class Parking(models.Model):
    # crea tabla en la base de datos, los atributos son las columnas de las tablas.
    title = models.CharField(max_length=50)
    address  = models.TextField()    
    price_hour = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)        
    price_day = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)        
    price_week = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)        
    price_year = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)        
    stock =  models.IntegerField()    
    avalaible = models.BooleanField(default=True)
    slug = models.SlugField(null=False, blank=False, unique=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    """
        MODIFICADO POR SIGNALS
    def save(self, *args, **kwargs):
        # Guarda el slug
        self.slug = slugify(self.title)
        super(Parking, self).save(*args, **kwargs)"""

    def __str__(self) -> str:
        return self.title

def set_slug(sender, instance, *args, **kwargs): # Debe recibir 5 elementos
    if instance.title and not instance.slug:
        slug = slugify(instance.title)

        
        # si existe algun objeto con ese slug, genera uno nuevo
        while Parking.objects.filter(slug=slug).exists():
            # pone caracteres aleatorios con la libreria uuid
            slug = slugify(
                '{}-{}'.format(instance.title, str(uuid.uuid4())[:8]  )
            )
        # La instancia es nuestro objeto almacenado
        instance.slug = slug
    
# Antes de que un objeto parking se almacene se ejecutra el callback set_slug
pre_save.connect(set_slug, sender=Parking)