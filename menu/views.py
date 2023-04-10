from .serializers import BlogSerialzier, CommentSerializer, MenuSerializer, TableReversedSerializer
from.models import Menu, Blog, Comment, TableReversed
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def menuList(request):
    menu = Menu.objects.all()
    serializer = MenuSerializer(menu, many=True)
    data = serializer.data
    for item in data:
        item['image_url'] = request.build_absolute_uri(item['image'])
        del item['image']
    return Response(data)

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
        return Response('Menu succsesfully delete!')
        
    

@api_view(['POST'])
def createMenu(request):
    serializer = MenuSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)




@api_view(['GET'])
def blogList(request):
    blog = Blog.objects.all()
    serializer = BlogSerialzier(blog, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createBlog(request):
    serializer = BlogSerialzier(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def blog_detail(request, id):
    if request.method == 'GET':
        blog = Blog.objects.get(id = id )
        serializer = BlogSerialzier(blog, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        blog = Blog.objects.get(id = id )
        serializer = BlogSerialzier(instance=blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'DELETE':
        blog = Blog.objects.get(id = id )
        blog.delete()
        return Response('Blog succsesfully delete!')





@api_view(['GET'])
def commentList(request):
    comment = Comment.objects.all()
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createComment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, id):
    if request.method == 'GET':
        comment = Comment.objects.get(id = id )
        serializer = CommentSerializer(comment, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        comment = Comment.objects.get(id = id )
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    elif request.method == 'DELETE':
        comment = Comment.objects.get(id = id )
        comment.delete()
        return Response('Comment succsesfully delete!')
    


@api_view(['GET'])
def TableReversedlist(request):
        table = TableReversed.objects.all()
        serializer = TableReversedSerializer(table, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def userWiseTable(request, id):
        table = TableReversed.objects.filter(user=id)
        serializer = TableReversedSerializer(table, many=True)
        return Response(serializer.data)