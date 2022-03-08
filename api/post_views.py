from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# models
from .models import Post
from .post_schema import PostSchema, PostCreateSchema
# serializers
from .serializers import PostSerializer


class PostList(APIView):
    """
    Queries and returns all post objects
    """

    schema = PostSchema()

    serializer_class = PostSerializer()

    # Get post data // retrieves post
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)



class PostCreateView(APIView):
    """
        The authenticated user creates a new post
        """
    schema = PostCreateSchema()
    serializer_class = PostSerializer()

    def post(self, request, format=None):

        data = request.data
        if request.user:
            data['author'] = request.user
            serializer = PostSerializer(data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "User not authenticated"})


class PostDetail(APIView):
    serializer_class = PostSerializer()
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)

        if request.user == post.author:
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':"You're not the owner of this post"},status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        if request.user == post.author:
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response({"message": "Not permitted"}, status=status.HTTP_400_BAD_REQUEST)
