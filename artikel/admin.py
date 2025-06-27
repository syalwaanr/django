from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import ArtikelBlog, Kategori, Komentar


# ✅ Custom Form untuk Artikel dengan CKEditor
class ArtikelForms(forms.ModelForm):
    isi = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = ArtikelBlog
        fields = '__all__'


# ✅ Admin untuk Artikel
class ArtikelBlogAdmin(admin.ModelAdmin):
    form = ArtikelForms  # pakai form CKEditor
    list_display = ('kategori', 'judul', 'created_at', 'created_by', 'status')
    search_fields = ('judul',)
    list_filter = ('status', 'kategori')
    list_per_page = 10


# ✅ Admin untuk Kategori
class KategoriAdmin(admin.ModelAdmin):
    list_display = ('nama', 'created_at', 'created_by')
    search_fields = ('nama',)


# ✅ Admin untuk Komentar
class KomentarAdmin(admin.ModelAdmin):
    list_display = ['nama', 'isi', 'artikel', 'tanggal']  # artikel bukan ArtikelBlog
    search_fields = ['nama']
    list_filter = ['artikel']


# ✅ Register semua ke admin
admin.site.register(Kategori, KategoriAdmin)
admin.site.register(ArtikelBlog, ArtikelBlogAdmin)
admin.site.register(Komentar, KomentarAdmin)
