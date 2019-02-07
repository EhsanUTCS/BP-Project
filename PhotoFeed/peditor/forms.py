from django import forms

class Crop_Form(forms.Form):
    a = forms.IntegerField(label='a')
    b = forms.IntegerField(label='b')
    c = forms.IntegerField(label='c')
    d = forms.IntegerField(label='d')
    fields = {
        'a' : a,
        'b' : b,
        'c' : c,
        'd' : d,
    }