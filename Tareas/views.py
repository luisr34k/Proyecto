from rest_framework import generics
from .models import Profesor, Mascota
from .serializers import ProfesorSerializer, MascotaSerializer  # Corrige la importación
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profesor
from .forms import ProfesorForm



# Vista para listar profesores
def listar_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'listar_profesores.html', {'profesores': profesores})

# Vista para agregar un nuevo profesor
def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_profesores')
    else:
        form = ProfesorForm()
    return render(request, 'agregar_profesor.html', {'form': form})

def modificar_profesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)
    
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('listar_profesores')  # Redirigir a la lista de profesores
    else:
        form = ProfesorForm(instance=profesor)
    
    return render(request, 'modificar_profesor.html', {'form': form})

class ProfesorListCreate(generics.ListCreateAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class MascotaListCreate(generics.ListCreateAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')  # Cambia a la vista del administrador
            else:
                return redirect('user_dashboard')   # Cambia a la vista del usuario
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    
    return render(request, 'login.html')

# Vista para listar profesores
def listar_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'listar_profesores.html', {'profesores': profesores})

# Vista para agregar un nuevo profesor
def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_profesores')
    else:
        form = ProfesorForm()
    return render(request, 'agregar_profesor.html', {'form': form})

@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('user_dashboard')
    return render(request, 'admin_dashboard.html')

@login_required
def user_dashboard(request):
    if request.user.is_superuser:
        return redirect('admin_dashboard')
    return render(request, 'user_dashboard.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'Hola.html')
