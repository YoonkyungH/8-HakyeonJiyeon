
from django.contrib import auth
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.core.serializers import serialize
from .forms import LoginForm, RegisterForm
import json
from .models import Customer
from orderrequest.models import OrderApply


def d_mypage_orderlist(request):
    if request.method == 'GET':
        order_list = OrderApply.objects.all()
        order_list = {'order_list' : order_list}
        return render(request, 'member/mypage_orderlist.html', order_list)

class IndexView(View):
    def get(self, request):
        users = Customer.objects.all().order_by('-id')
        data = json.loads(serialize('json', users))
        return JsonResponse({'users': data})
        
    def post(self, request):
        if request.META['CONTENT_TYPE'] == 'application/json':
            request = json.loads(request.body)
            user = Customer(
                cus_id = request['cus_id'],
                cus_pw = request['cus_pw'],
                cus_name = request['cus_name'],
                cus_address = request['cus_address'],
            )
        else:
            user = Customer(
                cus_id = request.POST['cus_id'],
                cus_pw = request.POST['cus_pw'],
                cus_name = request.POST['cus_name'],
                cus_address = request.POST['cus_address'],
            )

        user.save()
        return HttpResponse(status=200)

    def put(self, request):
        request = json.loads(request.body)
        id = request['id']
        cus_address = request['cus_address']
        user = get_object_or_404(Customer, pk=id)
        user.cus_address = cus_address  # 주소만 변경 가능하도록
        user.save()
        return HttpResponse(status = 200)

    def delete(self, request):
        request = json.loads(request.body)
        id = request['id']
        user = get_object_or_404(Customer, pk=id)
        user.delete()
        return HttpResponse(status = 200)

# http://127.0.0.1:8000/member/ -> GET으로 먼저 유저 목록을 확인한 뒤
# http://127.0.0.1:8000/member/login -> {"cus_id":"", "cus_pw":""} id와 pw를 POST로 보내기
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('main')
            else:
                return render(request, 'login.html', 
                    {'error': 'password is incorrect.', 'form': form}
                )
        else:
            return HttpResponse(status=400)
    else:
        return render(request, 'login.html', {'form': form})

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect('main')
    else:
        return HttpResponse(status=400)

# # 회원가입
def signup(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = Customer(
                username = cleaned_data.get('username'),
                password = cleaned_data.get('password'),
                cus_nickname = cleaned_data.get('nickname'),
                cus_address = cleaned_data.get('address'),
                cus_post_no = cleaned_data.get('post_no')
            )
            user.set_password(cleaned_data.get('password'))
            user.save()
            auth.login(request, user)
            return redirect('main')
        else:
            return HttpResponse(status=400)
    else:
        return render(request, 'register.html', {'form': form})

def review_rider_view(request): 
    return render(request, 'review_rider.html')

def review_cus_view(request):
    return render(request, 'review_cus.html')

def d_mypage_orderlist(request):
    order_list = OrderApply.objects.all()
    data = json.loads(serialize('json', order_list))
    return render(request, 'mypage_orderlist.html', {'orders': data})
    # return JsonResponse({'order_list': data})
    return render(request, 'mypage_orderlist.html')
