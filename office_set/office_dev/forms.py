from django.forms import *
from .models import InputJournal,Signature

class FormInputJournal(ModelForm):


    class Meta:

        model = InputJournal
        fields = "__all__"
        widgets = {
                    'numberInput':Select(attrs={'class': 'form-control'}),
                    'dateReg': TextInput(attrs={'class': "form-control", 'type': 'date', 'format': '%d.%m.%Y'}),
                    'correspondent': TextInput(attrs={'class': 'form-control'}),
                    'content': TextInput(attrs={'class': "form-control"}),
                    'executor': Select(attrs={'class': "form-control"}),
                    'mark': TextInput(attrs={'class': "form-control"}),
                    'nomenklatura': TextInput(attrs={'class': "form-control"}),
        }

class FormSignature(ModelForm):
    class Meta:
        model = Signature
        fields = "__all__"
        widgets = {
            'numberInput':TextInput(attrs={'class': 'form-control'}),
            'user':TextInput(attrs={'class': 'form-control'}),
            'datemark':TextInput(attrs={'class': 'form-control','type': 'date','format':'%d.%m.%Y'}),
        }
