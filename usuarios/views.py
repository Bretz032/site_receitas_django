from django.shortcuts import redirect, render
from django.contrib.auth.models import User


def login(request):
    return render(request,'usuarios/login.html')

def cadastro(request):
    if request.method=='POST':
        nome= request.POST['nome']
        email= request.POST['email']
        password= request.POST['password']
        password2= request.POST['password2']
        if not nome.strip():
            return redirect('cadastro')
        if not email.strip():
            return redirect('cadastro')   
        if password!= password2:
            return redirect('cadastro')   
        if User.objects.filter(email=email).exists():
            return redirect('cadastro')  
        user =User.objects.create_user(username=nome, email= email, password= password)
        user.save()
        print('Usuário cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')

def dashboard(request):
    return render(request,'usuarios/dashboard.html')

def logout(request):
    return render(request,'usuarios/logout.html')


