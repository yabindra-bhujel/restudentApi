from .serializers import MenuSerializer
from.models import Menu, Blog, Comment
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def menuList(request):
    menu = Menu.objects.all()
    serializer = MenuSerializer(menu, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def menu_detail(request, id):
    if request.method == 'GET':
        menu = Menu.objects.get(id = id )
        serializer = MenuSerializer(menu, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        menu = Menu.objects.get(id = id )
        serializer = MenuSerializer(instance=menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'DELETE':
        menu = Menu.objects.get(id = id )
        menu.delete()
        return Response('Item succsesfully delete!')
        
    

@api_view(['POST'])
def createMenu(request):
    serializer = MenuSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


