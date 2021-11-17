from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render

from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

import json
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import User
from django.core.serializers import serialize

# 로그인시 필요
from rest_framework.parsers import JSONParser


# django에 이 라이브러리들이 내장되어 있음

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             # cleaned_data: 유효성 검사를 통과한 클린한 데이터
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request=request, username=username, password=password)

#             if user is not None:
#                 login_view(request, user)
            
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#         return render(request, 'login.html', {'form' : form})

# def logout_view(request):
#     logout(request)
#     return redirect("home")


# # 회원가입
# def signup(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         return redirect('/')

#     # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
#     return render(request, 'login.html')


def d_mypage_orderlist(request):
    return render(request, 'member/mypage_orderlist.html')

def d_mypage(request):
    return render(request, 'member/mypage.html')
#         # if request.POST['password1'] == request.POST['password2']:
#         user = User.objects.create(
#             username = request.POST['username'],
#             password = request.POST['password'],
#             address = request.POST['address'],
#             # cus_id=request.POST['cus_id'],
#             # cus_pw=request.POST['cus_pw'],
#             # cus_name=request.POST['cus_name'],
#             # cus_address=request.POST['cus_address']
#             )
#         auth.login(request, user)
#         return redirect('index.html')
#     return render(request, 'signup.html')




class IndexView(View):
    def get(self, request):
        users = User.objects.all().order_by('-id')
        data = json.loads(serialize('json', users))
        return JsonResponse({'users': data})
        
    def post(self, request):
        if request.META['CONTENT_TYPE'] == 'application/json':
            request = json.loads(request.body)
            user = User(
                cus_id = request['cus_id'],
                cus_pw = request['cus_pw'],
                cus_name = request['cus_name'],
                cus_address = request['cus_address'],
            )
        else:
            user = User(
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
        user = get_object_or_404(User, pk=id)
        user.cus_address = cus_address  # 주소만 변경 가능하도록
        user.save()
        return HttpResponse(status = 200)

    def delete(self, request):
        request = json.loads(request.body)
        id = request['id']
        user = get_object_or_404(User, pk=id)
        user.delete()
        return HttpResponse(status = 200)

# http://127.0.0.1:8000/member/ -> GET으로 먼저 유저 목록을 확인한 뒤
# http://127.0.0.1:8000/member/login -> {"cus_id":"", "cus_pw":""} id와 pw를 POST로 보내기
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)  # rest_framework.parsers
        search_id = data['cus_id']
        obj = User.objects.get(cus_id = search_id)

        if data['cus_pw'] == obj.cus_pw:
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
