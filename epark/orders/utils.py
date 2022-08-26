from .models import Order

def get_or_create_order(reserve, request):
    order = Order.objects.filter(reserve=reserve).first()

    if order is None and request.user.is_authenticated:
        order = Order.objects.create(reserve=reserve, user= request.user)
    
    if order:
        request.session['order_id']= order.id

    return order