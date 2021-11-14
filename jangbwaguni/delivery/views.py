from django.shortcuts import render

# 배달원 등록
import json
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Rider
from django.core.serializers import serialize

# Create your views here.
def order_confirm_view(request):
    return render(request, 'delivery/order_confirm.html', {})

# http://127.0.0.1:8000/delivery/register/ -> POST로
# {"rider_id": "", "rider_pw": "", "rider_name": "", "rider_intro": "", "min_delivery_amount": } 형식으로 send
def register_rider_view(request):
    if request.method == 'POST':
        if request.META['CONTENT_TYPE'] == 'application/json':
            request = json.loads(request.body)
            rider = Rider(
                rider_id = request['rider_id'],
                rider_pw = request['rider_pw'],
                rider_name = request['rider_name'],
                min_delivery_amount=request['min_delivery_amount'],

                # 아래 필드들 어떻게 받을지.
                # rider_intro = request['rider_intro'],
                # rider_area = request['rider_area'],
                # rider_vehicle = request['rider_vehicle'],
                # bankbook = request['bankbook'],
                # license = request['license'],
                # recommended_person = request['recommended_person']
            )
        else:
            rider = Rider(
                rider_id=request.POST['rider_id'],
                rider_pw=request.POST['rider_pw'],
                rider_name=request.POST['rider_name'],
                min_delivery_amount=request.POST['min_delivery_amount'],

                # rider_intro=request.POST['rider_intro'],
                # rider_area=request.POST['rider_area'],
                # rider_vehicle=request.POST['rider_vehicle'],
                # bankbook=request.POST['bankbook'],
                # license=request.POST['license'],
                # recommended_person=request.POST['recommended_person']
            )
        rider.save()
        return HttpResponse(status=200)
    return render(request, 'delivery/register_rider.html', {})

def order_list_view(request):
    return render(request, 'delivery/order_list.html', {})