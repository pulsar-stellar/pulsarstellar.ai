from django.shortcuts import render


# DOCS VIEWS

def docs_view(request):
    return render(request, 'docs_templates/docs_view.html')
