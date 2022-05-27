from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Projeto, Tag, Perfil


class CriacaoUsuarioCustomizada(UserCreationForm):
	class Meta:
		model = User 
		fields = [
			'email',
            'password1',
			'password2',
			]
		labels = {
			'email': 'E-mail',
			'password1': 'Senha',
			'password2': 'Confirmação da senha'
		}

	def __init__(self, *args, **kwargs):
		super(CriacaoUsuarioCustomizada, self).__init__(*args, **kwargs)
		self.fields['email'].widget.attrs.update({'placeholder':('email@email.com')})
		self.fields['password1'].widget.attrs.update({'placeholder':('senha123!')})        
		self.fields['password2'].widget.attrs.update({'placeholder':('senha123!')})

		for name, field in self.fields.items():
			field.widget.attrs.update({'class': 'input'})


class EditarPerfilUsuarioCustomizada(ModelForm):
    class Meta:
        model = Perfil
        fields = [
			'nome', 'sobrenome', 'email', 'endereço',
            'bio', 'imagem_perfil', 'social'
		]

    def __init__(self, *args, **kwargs):
        super(EditarPerfilUsuarioCustomizada, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class FormCriarNovoProjeto(ModelForm):
	class Meta:
		model = Projeto
		fields = ['nome', 'descricao', 'thumbnail',
		 'imagem_demo', 'demo_link', 'tags']
		labels={
		'nome': 'Nome do projeto',
		'descricao': 'Descrição'
		}
	
	def __init__(self, *args, **kwargs):
		super(FormCriarNovoProjeto, self).__init__(*args, **kwargs)

		for name, field in self.fields.items():
			field.widget.attrs.update({'class': 'input'})