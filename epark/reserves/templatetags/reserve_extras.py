from django import template

# Registrar funciones como filters
register = template.Library()

@register.filter()
def quantity_parking_format(quantity=1):
    return '{} {}'.format(quantity, 'parkings' if quantity > 1 else 'parking')

@register.filter()
def quantity_add_format(quantity=1):
    return '{} {}'.format(
        quantity_parking_format(quantity),
        'agregados' if quantity > 1 else 'agregado'
     )
