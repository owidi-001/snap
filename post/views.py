from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# models
from .models import Post
from .schema import PostSchema
# serializers
from .serializers import PostSerializer


class PortView(APIView):
    """
    Queries and returns all post objects
    """
    schema = PostSchema()
    serializer_class = PostSerializer()

    #   TODO! Authentication classes
    

    # Get post data // retrieves post
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

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
