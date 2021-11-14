from django.shortcuts import render

# Create your views here.
def order_confirm_view(request):
    return render(request, 'delivery/order_confirm.html', {})

def register_rider_view(request):
    return render(request, 'delivery/register_rider.html', {})

def order_list_view(request):
    return render(request, 'delivery/order_list.html', {})