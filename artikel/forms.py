from django import forms  
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Kategori, ArtikelBlog

class KategoriForms(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ('nama',)
        widgets = {
            "nama": forms.TextInput(attrs={
                'class': 'form-control',
                'required': 'True' 
            }),
        }

class ArtikelForms(forms.ModelForm):
    isi = forms.CharField(widget=CKEditor5Widget(config_name='default'))

    class Meta:
        model = ArtikelBlog
        fields = ['judul', 'isi', 'kategori', 'gambar']
        widgets = {
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
            'kategori': forms.Select(attrs={'class': 'form-control'}),
            'gambar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }