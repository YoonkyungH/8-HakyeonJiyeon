from django.shortcuts import render

def d_order_cus(request):
    return render(request, 'order_cus.html')

def d_rider_list(request):
    return render(request, 'rider_list.html')