from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from projetos.models import Perfil, Projeto, Tag
from .serializers import ProjetoSerializer


# url/api/
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/projetos'},
        {'GET': '/api/projetos/id'},
        {'POST': '/api/projetos/token'},
        {'POST': '/api/projetos/token/refresh'},
    ]
    return Response(routes)
    # return JsonResponse(routes, safe=False)

# url/api/projetos/
@api_view(['GET'])
def getProjects(request):
    print('USER:', request.user)
    projects = Projeto.objects.all()
    serializer = ProjetoSerializer(projects, many=True)
    return Response(serializer.data)

# url/api/projetos/ID
@api_view(['GET'])
def getProject(request, pk):
    project = Projeto.objects.get(id=pk)
    serializer = ProjetoSerializer(project, many=False)
    return Response(serializer.data)