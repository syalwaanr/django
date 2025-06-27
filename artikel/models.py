from django.db import models
from django.contrib.auth.models import User
from django.utils.html import strip_tags
import html

class Kategori(models.Model):
    nama = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama


from django_ckeditor_5.fields import CKEditor5Field

class ArtikelBlog(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    judul = models.CharField(max_length=200)
    isi = CKEditor5Field('Konten', config_name='default')
    gambar = models.ImageField(upload_to='gambar_artikel/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def preview_text(self):
        return html.unescape(strip_tags(self.isi))[:200]

    def __str__(self):
        return self.judul


class Komentar(models.Model): 
    artikel = models.ForeignKey(ArtikelBlog, on_delete=models.CASCADE, related_name='komentar') 
    nama = models.CharField(max_length=100)
    isi = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Komentar oleh {self.nama} pada {self.artikel.judul}"
