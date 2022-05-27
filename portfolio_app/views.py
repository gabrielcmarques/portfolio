from django.shortcuts import render, redirect


def homePage(request):
    return render(request, "portfolio_app/homepage.html")


def aboutPage(request):
    if request.method == 'POST':
        return redirect('homepage')
    return render(request, "portfolio_app/sobre.html")