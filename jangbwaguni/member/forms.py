from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, Textarea
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password, make_password   # 비밀번호 암호화를 위해 django에서 제공하는 기능 추가

from .models import *


from member.models import *

class RegisterForm(forms.Form):
    username = forms.CharField(   # RegisterForm 내 email은 forms의 emailfield 에러 메시지 중 required가 나오면 해당 문자열 출력
        error_messages={
            'required' : '아이디를 입력해주세요.'
        },
        max_length=64, label='아이디'
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
    nickname = forms.CharField(
        error_messages={
            'required' : '닉네임을 입력해주세요.'
        },
        widget=forms.TextInput, label = '닉네임'
    )
    address = forms.CharField(
        error_messages={
            'required' : '닉네임을 입력해주세요.'
        },
        widget=forms.Textarea, label = '주소'
    )
    post_no = forms.CharField(
        error_messages={
            'required' : '우편번호를 입력해주세요.'
        },
        widget=forms.TextInput, label = '우편번호'
    )


    def clean(self):
        cleaned_data = super().clean()  # data 유효성 체크
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password: # 값은 있되 일치하지 않을 경우
                self.add_error('password', '비밀번호를 다시 확인해주세요.')
                self.add_error('re_password', '비밀번호를 다시 확인해주세요.')
                return
            else:
                return cleaned_data
        return 

class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required' : '이름을 입력해주세요.'
        },
        widget=forms.TextInput, label="이름"
    )
    address = forms.CharField(
        error_messages={
            'required' : '주소를 입력해주세요.'
        },
        widget=forms.Textarea, label = '주소'
    )

    def clean(self):
        cleaned_data = super().clean()  # data 유효성 체크
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')
        address = cleaned_data.get('address')

        if password and re_password:
            if password != re_password: # 값은 있되 일치하지 않을 경우
                raise forms.ValidationError("비밀번호를 다시 확인해주세요.")
        return cleaned_data


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Customer
        fields = ['username', 'password']


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
