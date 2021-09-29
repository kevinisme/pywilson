from django import forms

from wonder.models import Wonder


class WonderModelForm(forms.ModelForm):
    xdate = forms.DateField(required=True ,label='評估日期' ,
                            widget=forms.DateInput(attrs={'class':'form-control date' ,'autocomplete':'off'}))
    note = forms.CharField(required=True ,label='項目名稱' ,
                            widget=forms.TextInput(attrs={'class':'form-control'}))
    source = forms.CharField(required=False ,label='要求來源' ,
                            widget=forms.TextInput(attrs={'class':'form-control'}))
    xrange = forms.CharField(required=False ,label='價格區間' ,
                            widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Wonder
        fields = '__all__'
