from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from rest_framework.response import Response


from .models import *
class PostsView(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

@api_view(['GET'])
def postsList(request):
    posts = Posts.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def postGet(request, pk):
    posts = Posts.objects.get(pk=pk)
    serializer = PostSerializer(posts)
    return Response(serializer.data)


@api_view(['DELETE'])
def postDel(request, pk):
    posts = Posts.objects.get(pk=pk)
    posts.delete()
    return Response("Post deleted")

@api_view(['POST'])
def postCreate(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def postPatch(request, pk):
    post = Posts.objects.get(pk=pk)
    serializer = PostSerializer(data=request.data, instance=post, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def postPut(request, pk):
    post = Posts.objects.get(pk=pk)
    serializer = PostSerializer(data=request.data, instance=post, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)