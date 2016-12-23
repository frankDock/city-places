from django.shortcuts import render


def homepage(request):
    return render(request, template_name='static_pages/index.html')


def company(request):
    return render(request, template_name='static_pages/company.html')


def contact(request):
    return render(request, template_name='static_pages/contact.html')
