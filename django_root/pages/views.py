from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'pages/base.html')

def navbar(request):
    return render(request, 'pages/navbar.html')

def form_page(request):
    return render(request, 'pages/form.html')