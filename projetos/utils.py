from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.db.models import Q

from .forms import CriacaoUsuarioCustomizada
from .models import Projeto, Tag


def paginateProjects(request, projetos, results):
    page = request.GET.get('page')
    paginator = Paginator(projetos, results)

    try:
        projetos = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projetos = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projetos = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, projetos


def searchProjects(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(nome__icontains=search_query)

    projetos = Projeto.objects.distinct().filter(
        Q(nome__icontains=search_query) |
        Q(descricao__icontains=search_query) |
        Q(owner__nome__icontains=search_query) |
        Q(tags__in=tags)
    )
    return projetos, search_query


def mandarEmail(request):
    form = CriacaoUsuarioCustomizada(request.POST)
    email_user = request.POST.get('email')	
    messages.success(request, "Conta criada com sucesso! Por favor, confirme no seu email.")
    # EMAIL #
    subject = 'Seja bem vindo ao meu Website!'
    message = 'Estamos felizes que está conosco, seja bem-vindo[a]. (Posso configurar esse bot para enviar novidades do website, promoções, etc.)'

    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email_user],
            fail_silently=False,
        )
    except:
        print('ERRO AO ENVIAR O EMAIL!!!')