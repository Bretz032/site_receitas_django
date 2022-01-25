from django.shortcuts import redirect, render
 

def login(request):
    return render(request,'usuarios/login.html')

def cadastro(request):
    if request.method=='POST':
        print('Usuario criado com sucesso.')
        return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')

def dashboard(request):
    return render(request,'usuarios/dashboard.html')

def logout(request):
    return render(request,'usuarios/logout.html')


