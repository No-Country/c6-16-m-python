from .models import Order

def get_or_create_order(reserve, request):
    order = reserve.order

    if order is None and request.user.is_authenticated:
        order = Order.objects.create(reserve=reserve, user= request.user)
    
    if order:
        request.session['order_id']= order.order_id

    return order