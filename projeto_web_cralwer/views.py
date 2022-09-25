from multiprocessing import context
from .models import Artigo 
from .forms import ArtigoForm
from django.shortcuts import render, redirect
from .crawler import webCrawler

#localhost/crawler/
def homePage(request):
    msg = 'Teste mensagem. Ola Mundo HOME'
    context = {'msg': msg}
    return render(request, 'aplicacao/homepage.html', context)


#localhost/crawler/blog
def blogPage(request):
    msg = 'Teste mensagem. Ola Mundo BLOG'
    context = {'msg': msg}
    return render(request, 'aplicacao/blog.html', context)


#localhost/crawler/
def crawlerPage(request):
    links = Artigo.objects.order_by('url')
    form = ArtigoForm()

    context = {'links': links, 'form': form}
    return render(request, 'aplicacao/crawler.html', context)


#localhost/crawler/add
def crawlerAdd(request):
    Artigo.objects.all().delete()
    
    if request.method == 'POST':
        form = ArtigoForm(request.POST)
        if form.is_valid():                
            webCrawler(request.POST['url'])

    return redirect('crawler') 


#localhost/crawler/edit/id
def crawlerEdit(request, pk):
    artigo = Artigo.objects.get(id=pk)

    form = ArtigoForm(instance=artigo)

    if request.method == 'POST':
        form = ArtigoForm(request.POST, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('crawler')
    context = {'form': form, 'artigo': artigo}

    return render(request, 'aplicacao/editar.html', context)


#localhost/crawler/delete
def crawlerDelete(request, pk):
    artigo = Artigo.objects.get(id=pk)

    if request.method == 'POST':
        artigo.delete()
        return redirect('crawler')

    context = {'artigo': artigo}
    return render(request, 'aplicacao/delete.html', context)