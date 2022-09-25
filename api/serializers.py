from rest_framework import serializers
from projetos.models import Projeto, Perfil, Tag
from projeto_web_cralwer.models import Artigo


class PerfilSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Perfil
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProjetoSerializer(serializers.ModelSerializer):  
    owner = PerfilSerializer(many=False)  
    tags = TagSerializer(many=True)   

    class Meta:
        model = Projeto
        fields = '__all__'


class WebCrawlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artigo
        fields = '__all__'