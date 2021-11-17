from django import forms
from django.forms.widgets import PasswordInput
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password, make_password   # 비밀번호 암호화를 위해 django에서 제공하는 기능 추가

from .models import *


from member.models import *

class RegisterForm(forms.Form):
    email = forms.EmailField(   # RegisterForm 내 email은 forms의 emailfield 에러 메시지 중 required가 나오면 해당 문자열 출력
        error_messages={
            'required' : '이메일을 입력해주세요.'
        },
        max_length=64, label='이메일'
    )
    password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요.'
        },
        widget = forms.PasswordInput, label = '비밀번호'    # PasswordInput을 widget으로 지정
    )
    re_password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label = '비밀번호 확인'
    )

    def clean(self):
        cleaned_data = super().clean()  # data 유효성 체크
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password: # 값은 있되 일치하지 않을 경우
                self.add_error('password', '비밀번호를 다시 확인해주세요.')
                self.add_error('re_password', '비밀번호를 다시 확인해주세요.')
            else:
                user = Customer(    # User 데이터베이스에 저장
                    email = email,
                    password = password,
                )
                user.save()
                # member 저장 완료


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '이메일을 입력해주세요.'
        },
        max_length=64, label='이메일'
    )

    password = forms.CharField(
        error_messages={
            'required' : '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()  # data의 유효성 체크
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = Customer.objects.get(email=email)    # User의 email과 요청받은 email이 같은가
            except Customer.DoesNotExist:                   # User DB와 불일치
                self.add_error('email', '존재하지 않는 이메일입니다.')
                return

            if password != user.password:
            # if not check_password(password, user.password):
                self.add_error('password', '비밀번호를 다시 확인하세요.')
            else:
                self.email = user.email


# class RegisterRiderForm(forms.Form):
#     email = forms.EmailField(   # RegisterForm 내 email은 forms의 emailfield 에러 메시지 중 required가 나오면 해당 문자열 출력
#         error_messages={
#             'required': '이메일을 입력해주세요.'
#         },
#         max_length=64, label='이메일'
#     )
#     password = forms.CharField(
#         error_messages={
# #             'required': '비밀번호를 입력해주세요.'
#         },
#         widget=forms.PasswordInput, label='비밀번호'    # PasswordInput을 widget으로 지정
#     )
#     re_password = forms.CharField(
#         error_messages={
#             'required': '비밀번호를 입력해주세요.'
#         },
#         widget=forms.PasswordInput, label='비밀번호 확인'
#     )

#     def clean(self):
#         cleaned_data = super().clean()  # data 유효성 체크
#         email = cleaned_data.get('email')
#         password = cleaned_data.get('password')
#         re_password = cleaned_data.get('re_password')

#         if password and re_password:
#             if password != re_password:  # 값은 있되 일치하지 않을 경우
#                 self.add_error('password', '비밀번호를 다시 확인해주세요.')
#                 self.add_error('re_password', '비밀번호를 다시 확인해주세요.')
#             else:
#                 user = User(    # User 데이터베이스에 저장
#                     email=email,
#                     password=password,
#                 )
#                 user.save()
#                 # member 저장 완료
