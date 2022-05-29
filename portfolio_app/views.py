from django.shortcuts import render, redirect
from .models import PerfilHomepage


def homePage(request):
    perfil = PerfilHomepage.objects.all()
    context = {'perfil': perfil}
    return render(request, "portfolio_app/homepage.html", context)


def aboutPage(request):
    if request.method == 'POST':
        return redirect('homepage')
    return render(request, "portfolio_app/sobre.html")