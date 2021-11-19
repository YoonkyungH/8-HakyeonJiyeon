from django import forms
from .models import OrderApply

class OrderApplyForm(forms.ModelForm):
    class Meta:
        model = OrderApply # 사용할 모델
        fields = ['cus_orderer',
        
        'quantity', 'price',
        'order_name', 'order_phone', 'order_address', 'order_post',
            'order_additional']
