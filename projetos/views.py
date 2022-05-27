from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import CriacaoUsuarioCustomizada, EditarPerfilUsuarioCustomizada, FormCriarNovoProjeto
from .models import Projeto, Tag, Perfil
from .utils import searchProjects, paginateProjects, mandarEmail

#  TUDO VAI ESTAR BEM SIMPLES POR QUESTÃO DE DEMONSTRAÇÃO. NUMA VERSÃO REAL #
#  AS FUNÇÕES VÃO UTILIZAR DATABASES RELACIONAIS E TER MAIS FUNCIONALIDADES   #

# url/projetos #
def projetosHome(request):
	projetos, search_query = searchProjects(request)
	custom_range, projetos = paginateProjects(request, projetos, 3)

	context = {
			'projetos': projetos,
			'search_query': search_query,
			'custom_range': custom_range
			}
	return render(request, 'projetos/projetosHome.html', context)


# url/projetos/id # 
def projetoPage(request, pk):
    projUnico = Projeto.objects.get(id=pk)
    context = {'proj': projUnico}
    return render(request, 'projetos/projetoPage.html', context)


# url/projetos/login #
def loginUsuario(request):
	if request.method == 'POST':
		messages.success(request, 'Logado com sucesso!')
		return redirect('projetosHome')
	return render(request, 'projetos/loginUsuario.html')


# url/projetos/registro # 
def registroUsuario(request):	
	page = 'registroUsuario'
	form = CriacaoUsuarioCustomizada()
	
	if request.method == 'POST':		
		mandarEmail(request)
		
	context = {'page':page, 'form': form}
	return render(request, 'projetos/login_register.html', context)

#### CRUD PROJETOS ####

# url/projetos/criar-projeto/
def criarProjeto(request):
	form = FormCriarNovoProjeto()
	if request.method == 'POST':
		messages.success(request, "Projeto criado com sucesso!")
		return redirect('projetosHome')	
	context = {'form': form}
	return render(request, "projetos/form_projeto.html", context)

# url/projetos/editar-conta/ #
def editarConta(request):
	form = EditarPerfilUsuarioCustomizada()
	if request.method == 'POST':
		return redirect('projetosHome')
	context={'form': form}
	return render(request, 'projetos/editarConta.html', context)

# url/projetos/deletar-projeto/
def deletarProjeto(request):    
	if request.method == 'POST':
		messages.success(request, "Projeto deletado!")
		return redirect('projetosHome')
	return render(request, 'projetos/deletar_template.html')