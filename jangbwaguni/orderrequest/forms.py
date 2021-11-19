from django import forms
from .models import OrderApply

class OrderApplyForm(forms.ModelForm):
    class Meta:
        model = OrderApply # 사용할 모델
        fields = ['order_additional', 'cus_orderer','quantity']
