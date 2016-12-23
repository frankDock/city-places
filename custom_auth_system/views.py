from django.contrib.auth import logout
from django.shortcuts import render


def logout_user(request):
    logout(request)
    return render(request, template_name='static_pages/index.html')
