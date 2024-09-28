# urls.py en la aplicación Tareas
from django.urls import path
from .views import ProfesorListCreate, MascotaListCreate, user_login, user_logout, admin_dashboard, user_dashboard, listar_profesores, modificar_profesor
from . import views

urlpatterns = [
    path('profesores/', ProfesorListCreate.as_view(), name='profesores'),
    path('mascotas/', MascotaListCreate.as_view(), name='mascotas'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('user-dashboard/', user_dashboard, name='user_dashboard'),  
    path('profesores/agregar/', views.agregar_profesor, name='agregar_profesor'),
    path('profesores/listar/', listar_profesores, name='listar_profesores'),
    path('profesores/modificar/<int:id>/', modificar_profesor, name='modificar_profesor'),
]
