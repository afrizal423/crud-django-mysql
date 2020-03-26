from django.shortcuts import render, redirect
from .models import Biodata, JenjangPendidikan, Pendidikan
from datetime import datetime
from .forms import BioForm, PendidikanForm
# Create your views here.
def emp(request):
    bio = Biodata.objects.all()
    # print(bio)
    for u in bio:
        age = int((datetime.now().date() - u.tgl_lahir).days / 365.25)
    
    didik = Pendidikan.objects.all().select_related('id_jenjang')
    for x in didik:
        print(x.id_jenjang.nama_jenjang)
    # print(didik.id_jenjang.nama_jenjang)
    print(age)
    
    data = {
        'judul':'CRUD With Django',
        'bio':bio,
        'umur':age,
        'didik':didik
    }   
    return render(request,"index.html",data)  

def tmbhjenjang(request):
    bio = Biodata.objects.all().first()
    jenjang = JenjangPendidikan.objects.all()
    data = {
        'bio':bio,
        'jenjang':jenjang,
    }
    if request.method == 'POST':
        form = PendidikanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        pass
    return render(request,"tmbhjenjang.html",data)

def edit(request, id):
    npm = Biodata.objects.get(npm=id)
    data = {
        'judul':'Edit biodataku',
        'bio':npm
    }
    print(data)
    if request.method == 'POST':
        form = BioForm(request.POST, instance = npm)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,"editbio.html",data)

# def updatebio(request,id):
#     npm = Biodata.objects.get(npm=id)  
#     form = BioForm(request.POST, instance = npm)
#     if form.is_valid():
#         form.save()
#         return redirect("/")
#     return render(request,"editbio.html",data = npm)

def editjenjang(request, id):
    dt = Pendidikan.objects.get(id_pendidikan=id)
    jenjang = JenjangPendidikan.objects.all()
    bio = Biodata.objects.all().first()
    data = {
        'judul':'Edit Jenjang Pendidikan',
        'data':dt,
        'jenjang':jenjang,
        'bio':bio
    }
    print(dt.nama_sekolah)
    if request.method == 'POST':
        form = PendidikanForm(request.POST, instance = dt)
        if form.is_valid():
            form.save()
            return redirect("/")
        pass
    return render(request,"editjenjang.html",data)

# def updatejenjang(request,id):
#     dt = Pendidikan.objects.get(id_pendidikan=id)  
#     form = PendidikanForm(request.POST, instance = dt)
#     if form.is_valid():
#         form.save()
#         return redirect("/")
#     return render(request,"editjenjang.html",data = dt)

def hapusjenjang(request, id):
    dt = Pendidikan.objects.get(id_pendidikan=id)
    dt.delete()
    return redirect("/")

    