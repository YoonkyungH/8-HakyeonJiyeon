
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
from .models import Customer, Rider
from orderrequest.models import OrderApply, EvalCustomer, EvalRider



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

def review_rider_view(request, rider_id):
    rider = get_object_or_404(Rider, pk=rider_id)

    if request.method == 'POST':
        speed_value = int(request.POST.get('speed'))
        fresh_value = int(request.POST.get('fresh'))
        accuracy_value = int(request.POST.get('accuracy'))
        evaluation = EvalRider.objects.filter(rider=rider, evaluator=request.user).first()
        if evaluation is not None:
            evaluation.speed = speed_value
            evaluation.fresh = fresh_value
            evaluation.accuracy = accuracy_value
            evaluation.save()
        else:
            evaluation = EvalRider(rider=rider, evaluator=request.user, 
                speed=speed_value, fresh=fresh_value, accuracy=accuracy_value)
            evaluation.save()

    evaluations = EvalRider.objects.filter(rider=rider)

    speed_star = "★☆☆"
    fresh_star = "★★☆"
    accuracy_star = "★☆☆"
    return render(request, 'review_rider.html', {'rider':rider, 'evaluations':evaluations, 
        'speed':"".join(speed_star), 'fresh':"".join(fresh_star), 'accuracy':"".join(accuracy_star)})

def review_cus_view(request, cus_id=None, score=None):
    customer = get_object_or_404(Customer, pk=cus_id)
    rider = get_object_or_404(Rider, rider_nickname=request.user)
    if score and score >= 0 and score <= 2:
        evaluation = EvalCustomer.objects.filter(customer=customer, evaluator=rider).first()
        if evaluation is not None:
            evaluation.score = score
            evaluation.save()
        else:
            evaluation = EvalCustomer(customer=customer, evaluator=rider, score=score)
            evaluation.save()

    evaluations = EvalCustomer.objects.filter(customer=customer)
    avg_score = 3.2

    return render(request, 'review_cus.html', {'customer': customer, 'evaluations': evaluations, 'score': avg_score})



def d_mypage_orderlist(request):
    order_list = OrderApply.objects.filter(cus_orderer=request.user)
    if order_list is not None:
        order_list = order_list.order_by('-created_at')
    rider = Rider.objects.filter(rider_nickname=request.user).first()
    if rider is not None:
        delivery_list = OrderApply.objects.filter(rider_selected=rider)
    else:
        delivery_list = None
    return render(request, 'mypage_orderlist.html', {'orders': order_list, 'deliveries': delivery_list})

