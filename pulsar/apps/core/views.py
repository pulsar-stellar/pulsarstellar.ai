from django.shortcuts import render


# CORE VIEWS

def core_home(request):
    return render(request, 'core_templates/views/core_home.html')

def core_about(request):
    return render(request, 'core_templates/views/core_about.html',  {'title': 'About'})


def core_research(request):
    return render(request, 'core_templates/views/core_research.html',  {'title': 'Research'})


# ERRORS VIEWS

def page_not_found(request, exception):
    return render(request, "core_templates/errors/404.html", {})

def error(request, exception=None):
    return render(request, "core_templates/errors/500.html", {})

def permission_denied(request, exception=None):
    return render(request, "core_templates/errors/403.html", {})

def bad_request(request, exception=None):
    return render(request, "core_templates/errors/400.html", {})