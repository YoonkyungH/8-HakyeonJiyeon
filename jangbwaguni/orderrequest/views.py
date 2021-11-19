
from django.http import JsonResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
import datetime
from django.urls import reverse 

# from delivery.models import Rider
from member.models import Customer, Rider
from orderrequest.models import OrderApply
from .forms import OrderApplyForm
# View
import json
from django.views import View
from django.core.serializers import serialize
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import serializers
from delivery.serializers import DeliverySerializer

from django.views.decorators.csrf import csrf_exempt # 추후 삭제

# 성공-----------------------------------------------------
# def d_order_cus(request, cus_id, rider_id):
#     rider = get_object_or_404(Rider, pk=rider_id) # Rider클래스에서 가지는 pk값이 아니면 404에러 발생
#     cus = get_object_or_404(Customer, pk=cus_id)
#     # rider_list = Rider.objects.all().filter(id=rider_id) # Rider값 중 pk값에 해당하는 object만 넘겨줌
#     form = OrderApplyForm()
#     if request.method == 'POST':
#         form = OrderApplyForm(request.POST)
#         if form.is_valid():
#             new_order = form.save(commit=False)
#             new_order.created_at = timezone.now()
#             # new_order.cus_orderer = 
#             new_order.rider_selected = rider
#             new_order.cus_orderer = cus
#             # new_order.quantity = request.POST.getlist("quantity[]")
#             new_order.product = request.POST.getlist("product[]")
#             new_order.sale_store = request.POST.getlist("sale_store[]")
#             new_order.save()
#             return render(request, 'member/mypage_orderlist.html')
            
#     else:
#         form = OrderApplyForm()
#     context = {'form':form}
#     return render(request, 'orderrequest/order_cus.html', {'form':form, 'rider':rider, 'cus':cus})
# 성공------------------------------------------------
# @login_required
# @csrf_exempt
def d_order_cus(request, rider_id):
    rider = get_object_or_404(Rider, pk=rider_id) # Rider클래스에서 가지는 pk값이 아니면 404에러 발생
    # cus = Customer.objects.all().filter(id=user)
    form = OrderApplyForm()
    if request.method == 'POST':
        form = OrderApplyForm(request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.created_at = timezone.now()
            # new_order.cus_orderer = 
            new_order.rider_selected = rider
            new_order.cus_orderer = request.user
            # new_order.quantity = request.POST.getlist("quantity[]")
            new_order.product = request.POST.getlist("product[]")
            new_order.sale_store = request.POST.getlist("sale_store[]")
            new_order.save()
            return render(request, 'member/mypage_orderlist.html')
    else:
        form = OrderApplyForm()
    context = {'form':form}
    return render(request, 'orderrequest/order_cus.html', {'form':form, 'rider':rider})

def d_rider_list(request):
    rider_list = Rider.objects.all() # Rider 클래스의 데이터 가져옴
    return render(request, 'orderrequest/rider_list.html', {'rider_list':rider_list})

# 성공------------------------------------------------
#### 하단의 IndexView와 동일한 기능
# def d_rider_list(request, cus_id):
#     cus_list = get_object_or_404(Customer, pk=cus_id) # Customer클래스에서 가지는 pk값이 아니면 404에러 발생
#     rider_list = Rider.objects.all() # Rider 클래스의 데이터 가져옴
#     # order_list
#     # order_product = order_list.product
#     # output = ', '.join([q.product for q in order_product])
#     return render(request, 'orderrequest/rider_list.html', {'cus_list':cus_list,'rider_list':rider_list})
# 성공------------------------------------------------
    # if request.method == 'GET':
    #     riders = Rider.objects.all()
    #     serializer = DeliverySerializer(riders, many=True)
    #     return JsonResponse(serializer.data, safe=False)
    # elif request.method == 'POST':
        # data = JSONParser().parse(request)
        # serializer = DeliverySerializer(data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse(serializer.data, status=201)
        # return JsonResponse(serializer.errors, status=400)
 
# def d_order_cus(request, rider_id):
#     rider = get_object_or_404(Rider, pk=rider_id) # Rider클래스에서 가지는 pk값이 아니면 404에러 발생
#     rider_list = Rider.objects.all().filter(id=rider_id) # Rider값 중 pk값에 해당하는 object만 넘겨줌
#     # cus_list = Customer.objects.all().filter(id=cus_id)

#     # rider_list = Rider.objects.get(id=rider_id)

#     ######################################3# 유효성 검사 추가 안함
#     # POST 방식일 때
#     if request.method == 'POST':
#         new_order = OrderApply()  
#         new_order.quantity = request.POST['input-quantity']
#         new_order.product = request.POST['input-item']
#         new_order.sale_store = request.POST['input-store']
#         new_order.price = request.POST['inputprice']
#         new_order.created_at = datetime.datetime.now()
#         # new_order.save(commit=False)
#         # new_order.rider_selected = rider_selected
#         new_order.rider_selected = request.POST['rider-select']
#         # new_order.cus_orderer = request.POST[cus_orderer]
#         new_order.order_name = request.POST['input-cus']
#         new_order.order_phone = request.POST['input-phone']
#         new_order.order_address = request.POST['input-adress']
#         new_order.order_post = request.POST['input-post']
#         new_order.order_additional = request.POST['input-etc']
        
#         new_order.save()
#         # return redirect('d_mypage_orderlist', cus_id)
#         return render(request, 'member/mypage_orderlist.html')
#     # GET 방식일 때
#     else:
#         new_order = OrderApply.objects.all()
#         return render(request, 'orderrequest/order_cus.html', {'rider_list':rider_list})

#     # return redirect ('d_mypage_orderlist', cus_id)
#     # return redirect('order_list', customer.id)





#### 상단의 d_rider_list와 동일한 기능
# class IndexView(View):
#     template_name = 'orderrequest/rider_list.html'
#     # context_object_name = 'latest_question_list'

#     def get(self, request): # 배달원 목록 불러오기(모든 정보포함)
#         # data = json.loads(serialize('json', rider_list))
#         # return JsonResponse({'rider_list': data})

#         rider_list = Rider.objects.all()
#         # data = json.loads(serialize('json', rider_list))
#         # return JsonResponse({'rider_list': data})
#         # data = JSONParser().parse(request)
#         # serializer = DeliverySerializer(data=data)
#         return render(request, 'orderrequest/rider_list.html', {'rider_list':rider_list})

