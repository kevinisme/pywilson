from django import forms

from receipt.models import Receipt


class ReceiptModelForm(forms.ModelForm):
    ydate = forms.DateField(required=True ,label='日期' ,
                            widget=forms.DateInput(attrs={'class':'form-control date' ,'autocomplete':'off'}))
    itemname = forms.CharField(required=True ,label='項目名稱' ,
                            widget=forms.TextInput(attrs={'class':'form-control'}))
    code = forms.CharField(required=True ,label='收據號碼' ,
                            widget=forms.TextInput(attrs={'class':'form-control'}))
    shop = forms.CharField(required=False ,label='店家名稱' ,
                            widget=forms.TextInput(attrs={'class':'form-control'}))
    price = forms.IntegerField(required=True ,label='價格' ,
                            widget=forms.NumberInput(attrs={'class':'form-control'}))

    class Meta:
        model = Receipt
        fields = '__all__'
