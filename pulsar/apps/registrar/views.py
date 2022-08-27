from django.shortcuts import render


# REGISTRAR VIEWS

def registrar_register(request):
    return render(request, 'registrar_templates/views/register.html', {'title': 'Register'})


def registrar_login(request):
    return render(request, 'registrar_templates/views/login.html', {'title': 'Login'}) 