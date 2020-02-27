from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serilizers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serilizers.HelloSerilizers

    def get(self, request, format=None):
        """return a list of APIView features"""
        an_apiview = [
            'uses http methods as function (get, post, patch, put, delete)',
            'is similar to a traditional django view',
            'gives you the most control over you application logic',
            'is mapped manually to url'
                      ]
        return Response({'message': 'hello', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello message with out name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle Update an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """handle partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'method': 'DELETE'})





