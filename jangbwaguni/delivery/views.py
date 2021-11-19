from django.shortcuts import render

# 배달원 등록
import json
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.core.serializers import serialize
from member.models import Rider, Customer
from orderrequest.models import OrderApply

from django.views.decorators.csrf import csrf_exempt

from member.models import Rider

# TEST
from django.core.serializers import serialize
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .serializers import DeliverySerializer

# Create your views here.
def order_confirm_view(request, pk):    # 들어온 주문을 확인
    obj = Customer.objects.get(pk=pk)     # 지정된 배달원

    if request.method == 'GET':
        serializer = DeliverySerializer(obj)
        data = json.loads(serialize('json', serializer))
        # return HttpResponse(status=200)
        # return JsonResponse(serializer.data, safe=False)
        return render(request, 'delivery/order_confirm.html', {})


# def order_confirm_view(request):
#     if request.method == 'GET':
#         order_list = orders.objects.all()
#         list = {'order_list': order_list}
#         return render(request, 'delivery/order_confirm.html', list)
#         # data = json.loads(serialize('json', order_list))
        
#         return render(request, 'delivery/order_confirm.html', {})


def order_confirm_view(request):
    if request.method == 'GET':
        order_list = Customer.objects.all()
        list = {'order_list': order_list}
        return list


# http://127.0.0.1:8000/delivery/register/ -> POST로
# {"rider_id": "", "rider_pw": "", "rider_name": "", "rider_intro": "", "min_delivery_amount": } 형식으로 send
@csrf_exempt
def register_rider_view(request):   # 라이더 등록
    if request.method == 'GET':
        rider_list = Rider.objects.all()
        data = json.loads(serialize('json', rider_list))
        # return JsonResponse({'rider_lsit': data})
        return render(request, 'delivery/register_rider.html', {})


    if request.method == 'POST':
        if request.META['CONTENT_TYPE'] == 'application/json':
            request = json.loads(request.body)
            rider = Rider(
                # rider_id = request['rider_id'],
                # rider_pw = request['rider_pw'],
                rider_name = request['rider_name'],
                min_delivery_amount=request['min_delivery_amount'],
                rider_intro = request['rider_intro'],
                recommended_person=request['recommended_person'],
                rider_area = request.POST('rider_area'),
                # bankbook = request['bankbook'],
                # license = request['license'],


                # multiselectfield(여러개 값을 받야아 하는) 체크박스 값이 잘 post되는지 테스트 필요
                # rider_vehicle = request.POST.getlist('input태그 id값')
                # rider_vehicle = request.POST.getlist('vehicle')
                # rider_vehicle = request.POST.getlist('input태그 name값[]')
                rider_vehicle=request.POST.getlist('vehicle[]'),


                # rider_vehicle = request['rider_vehicle'],
            )
        else:
            rider = Rider(
                # rider_id=request.POST['rider_id'],
                # rider_pw=request.POST['rider_pw'],
                rider_name=request.POST['rider_name'],
                min_delivery_amount=request.POST['min_delivery_amount'],
                rider_intro = request.POST['rider_intro'],
                recommended_person=request.POST['recommended_person'],
                rider_area=request.POST['rider_area'],
                # bankbook=request.POST['bankbook'],
                # license=request.POST['license'],

                # rider_vehicle = request.POST.getlist('vehicle')
                # rider_vehicle=request.POST['rider_vehicle'],
                rider_vehicle=request.POST.getlist('vehicle[]'),
            )
        rider.save()
        return HttpResponse(status=200)
        # return render(request, 'delivery/register_rider.html', {})


def order_list_view(request):   # 선착순 주문 목록
    # if request.method == 'GET': # 주문 목록
        # order_list = orders.objects.all()
        # data = json.loads(serialize('json', order_list))
        # return JsonResponse({'order_list': data})
    #     return render(request, 'delivery/order_list.html', {})

    # TEST 후 이 주석 풀어주면 됨
    # if request.method == 'GET':
    #     # all_orders = orders.objects
    #     order_list = orders.objects.all()
    #     # order_list = all_orders.all()
    #     list = {'order_list': order_list}
    #     return render(request, 'delivery/order_list.html', list)

    # TEST(이것도 됨)
    if request.method == 'GET':
        order_list = OrderApply.objects.values()
        order_list = {'order_list': order_list}
        # order = order_list.get()
        # orders.objects.value()[0]
        return render(request, 'delivery/order_list.html', order_list)


# def order_list_view(request, pk):
#     obj = orders.objects.get(pk=pk)

#     if request.method == 'GET':
#         serializer = DeliverySerializer(obj)
    
#         return JsonResponse(serializer.data, safe=False)

    # if request.method == 'GET':
    #     order_list = orders.objects.all()
    #     list = {'order_list': order_list}
    #     return render(request, 'delivery/order_list.html', list)


# orderrequest로 옮김
#     if request.method == 'POST':    # 주문하기
#         if request.META['CONTENT_TYPE'] == 'application/json':
#             request = json.loads(request.body)
#             order_list = orders(
#                 cus_name = request['cus_name'],
#                 cus_address = request['cus_address'],
#                 # order_product
#                 cus_call = request['cus_call'],
#                 order_message = request['order_message'],
#             )
#         else:
#             order_list = orders(
#                 cus_name = request.POST['cus_name'],
#                 cus_address = request['cus_address'],
#                 # order_product
#                 cus_call = request['cus_call'],
#                 order_message = request['order_message'],
#             )
#         order_list.save()
#         return HttpResponse(status=200)
#         # return render(request, 'delivery/order_list.html', {})

