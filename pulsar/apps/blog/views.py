from django.shortcuts import render


# BLOG VIEWS

def blog_home(request):
    return render(request, 'blog_templates/views/blog_home.html')
