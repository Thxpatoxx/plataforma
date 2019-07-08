from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm,Nuevo_ProdForm,Nuevo_ServForm,Nuevo_EditServForm,Nuevo_EditProdForm
from django.shortcuts import render, get_object_or_404,redirect
from .models import Producto,Modelo,Servicio
from django.db.models import Count
import os

def home(request):
    posts = Modelo.objects.order_by('codigo')
    return render(request, 'home.html', {'posts': posts})
def stock(request):
    posts = Producto.objects.all()
    return render(request, 'stock.html', {'posts': posts})
def servicio(request):
    posts = Servicio.objects.all()
    return render(request, 'servicios.html', {'posts': posts})
##################################################################
def compra(request, pk):
    post = get_object_or_404(Producto, pk=pk)
    return render(request, 'compra.html', {'post': post})
def serv_det(request, pk):
    post = get_object_or_404(Servicio, pk=pk)
    return render(request, 'serv_det.html', {'post': post})
###################################################################
def nuevo_prod(request):
    if request.method == "POST":
        form = Nuevo_ProdForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('compra', pk=post.pk)
    else:
        form = Nuevo_ProdForm()
    return render(request, 'nuevo_prod.html', {'form': form})
def nuevo_serv(request):
    if request.method == "POST":
        form = Nuevo_ServForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.tecnico = request.user
            post.cant_pers = '1'
            post.precio = '1'
            post.estado = 'PENDIENTE'
            post.descripcion_tecnico = 'PENDIENTE'
            post.save()
            return redirect('serv_det', pk=post.pk)
    else:
        form = Nuevo_ServForm()
    return render(request, 'nuevo_serv.html', {'form': form})
###################################################################
def edit_serv(request, pk):
    post = get_object_or_404(Servicio, pk=pk)
    if request.method == "POST":
        form = Nuevo_EditServForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('servicio')
    else:
        form = Nuevo_EditServForm(instance=post)
    return render(request, 'nuevo_serv.html', {'form': form})
def edit_prod(request, pk):
    post = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = Nuevo_EditProdForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.estado = 'NO DISPONIBLE'
            post.save()
            return redirect('stock')
    else:
        form = Nuevo_EditProdForm(instance=post)
    return render(request, 'prod_edit.html', {'form': form})
###################################################################
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'