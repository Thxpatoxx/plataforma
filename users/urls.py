from django.urls import path
from .views import SignUpView
from . import views
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new

urlpatterns = [
    path('', views.home, name='home'),
    path('stock/', views.stock, name='stock'),
    path('Servicio/', views.servicio, name='servicio'),
    path('Compra/<int:pk>/', views.compra, name='compra'),
    path('Servicio/<int:pk>/', views.serv_det, name='serv_det'),
    path('Agregar_Producto', views.nuevo_prod, name='nuevo_prod'),
    path('Agregar_Servicio', views.nuevo_serv, name='nuevo_serv'),
    path('Servicio/<int:pk>/Editar/', views.edit_serv, name='edit_serv'),
    path('signup/', SignUpView.as_view(), name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)