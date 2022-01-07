from django import forms

from contatos.models import Contato


class ContatoForm(forms.ModelForm):
    email = forms.EmailField(label=Contato._meta.get_field('email').verbose_name,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(label=Contato._meta.get_field('telefone').verbose_name,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_aniversario = forms.DateTimeField(label=Contato._meta.get_field('data_aniversario').verbose_name,
                                           widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
    peso = forms.FloatField(label=Contato._meta.get_field('peso').verbose_name,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Contato
        fields = ('email', 'telefone', 'data_aniversario', 'peso',)
