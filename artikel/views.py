from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import ArtikelBlog, Kategori
from artikel.forms import KategoriForms, ArtikelForms
from django.contrib.auth.models import User
# ==================== Halaman Umum ====================
def home(request):
    kategori = Kategori.objects.all()
    kategori_id = request.GET.get('kategori')
    artikel_list = ArtikelBlog.objects.filter(kategori__id=kategori_id) if kategori_id else ArtikelBlog.objects.all()
    return render(request, 'home.html', {
        'ArtikelBlog_list': artikel_list,
        'kategori': kategori
    })

def detail_artikel(request, id):
    artikel = get_object_or_404(ArtikelBlog, id=id)
    artikel_lainya = ArtikelBlog.objects.exclude(id=id)[:3]
    return render(request, 'landingpage/detail.html', {
        'artikel': artikel,
        'artikel_lainya': artikel_lainya
    })

def about_author(request):
    return render(request, 'cv.html')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/auth-login')
    return render(request, "dashboard/index.html", {
        "title": "Selamat Datang"
    })


def artikel_list(request):
    artikel = ArtikelBlog.objects.all()
    return render(request, "dashboard/artikel_list.html", {
        "title": "Selamat Datang",
        "artikel": artikel
    })
# ==================== Kategori (Admin) ====================
@login_required(login_url='/auth-login')
def admin_kategori_list(request):
    kategori = Kategori.objects.all()
    return render(request, "dashboard/admin/kategori_list.html", {
        "kategori": kategori
    })

@login_required(login_url='/auth-login')
def admin_kategori_tambah(request):
    form = KategoriForms(request.POST or None)
    if request.method == "POST" and form.is_valid():
        kategori = form.save(commit=False)
        kategori.created_by = request.user
        kategori.save()
        return redirect(admin_kategori_list)
    return render(request, "dashboard/admin/kategori_forms.html", {
        "form": form
    })

@login_required(login_url='/auth-login')
def admin_kategori_update(request, id_kategori):
    kategori = get_object_or_404(Kategori, id=id_kategori)
    form = KategoriForms(request.POST or None, instance=kategori)
    if request.method == "POST" and form.is_valid():
        kategori = form.save(commit=False)
        kategori.created_by = request.user
        kategori.save()
        return redirect(admin_kategori_list)
    return render(request, "dashboard/admin/kategori_forms.html", {
        "form": form
    })

@login_required(login_url='/auth-login')
def admin_kategori_delete(request, id_kategori):
    kategori = get_object_or_404(Kategori, id=id_kategori)
    kategori.delete()
    return redirect(admin_kategori_list)

# ==================== Artikel Blog (Admin) ====================
@login_required(login_url='/auth-login')
def admin_artikel_list(request):
    artikel = ArtikelBlog.objects.all()
    return render(request, "dashboard/admin/artikel_list.html", {
        "artikel": artikel
    })

@login_required(login_url='/auth-login')
def admin_artikel_tambah(request):
    template_name = "dashboard/admin/artikel_forms.html"
    if request.method == "POST":
        forms = ArtikelForms(request.POST, request.FILES)
        print(forms.errors)
        if forms.is_valid():
            pub = forms.save(commit=False)
            pub.created_by = request.user
            pub.save()
        return redirect(admin_artikel_list)
    forms = ArtikelForms()
    context = {
        "forms": forms
    }
    return render(request, template_name, context)

@login_required(login_url='/auth-login')
def admin_artikel_update(request, id_artikel):
    artikel = get_object_or_404(ArtikelBlog, id=id_artikel)
    forms = ArtikelForms(request.POST or None, request.FILES or None, instance=artikel)
    if request.method == "POST" and forms.is_valid():
        artikel = forms.save(commit=False)
        artikel.created_by = request.user
        artikel.save()
        return redirect('admin_artikel_list')
    return render(request, "dashboard/admin/artikel_forms.html", {
        "forms": forms
    })

@login_required(login_url='/auth-login')
def admin_artikel_delete(request, id_artikel):
    artikel = get_object_or_404(ArtikelBlog, id=id_artikel)
    artikel.delete()
    return redirect('admin_artikel_list')

# ==================== Management User (Admin) ====================
@login_required(login_url='/auth-login')
def admin_management_user_list(request):
    template_name = "dashboard/admin/user_list.html"
    daftar_user = User.objects.all()
    context = {
        "daftar_user":daftar_user
    }
    return render(request, template_name, context)
