from django.core import serializers
from django.core.serializers import serialize
from django.core.serializers.base import Serializer
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Rider

from member.models import Customer


# View
import json
from django.views import View
from delivery.models import orders
from django.core.serializers import serialize
from delivery.serializers import DeliverySerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


from rest_framework import serializers

# delivery에서 옮긴 주문 기능
def d_order_cus(request):
    if request.method == 'GET':  # 주문 목록
        order_list = orders.objects.all()
        data = json.loads(serialize('json', order_list))
        return JsonResponse({'order_list': data})

    if request.method == 'POST':    # 주문하기
        if request.META['CONTENT_TYPE'] == 'application/json':
            request = json.loads(request.body)
            order_list = orders(
                cus_name=request['cus_name'],
                cus_address=request['cus_address'],
                # order_product
                cus_call=request['cus_call'],
                order_message=request['order_message'],
            )
        else:
            order_list = orders(
                cus_name=request.POST['cus_name'],
                cus_address=request['cus_address'],
                # order_product
                cus_call=request['cus_call'],
                order_message=request['order_message'],
            )
        order_list.save()
        return HttpResponse(status=200)
        # return render(request, 'delivery/order_list.html', {})
    return render(request, 'orderrequest/order_cus.html')

def d_rider_list(request):
    return render(request, 'orderrequest/rider_list.html')

class IndexView(View):
    def get(self, request): # 배달원 목록 불러오기(모든 정보포함)
        # rider_list = Rider.objects.all()
        # data = json.loads(serialize('json', rider_list))
        # return JsonResponse({'rider_list': data})


        rider_list = Rider.objects.all()
        data = json.loads(serialize('json', rider_list))
        # return JsonResponse({'rider_list': data})
        return render(request, 'orderrequest/rider_list.html')
        



#### 예제
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)
