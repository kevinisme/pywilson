from django import forms

from twinbird.models import Twinbird


class TwinbirdModelForm(forms.ModelForm):

    class Meta:
        model = Twinbird
        fields = '__all__'
        widgets = {'wonderid':forms.HiddenInput()}
        widgets = {'dogid':forms.HiddenInput()}
        widgets = {'catid':forms.HiddenInput()}
        widgets = {'eggid':forms.HiddenInput()}
        widgets = {'wondernote':forms.HiddenInput()}
        widgets = {'dogitemname':forms.HiddenInput()}
        widgets = {'catitemname':forms.HiddenInput()}
        widgets = {'eggitemname':forms.HiddenInput()}




