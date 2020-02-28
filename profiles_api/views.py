from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


from profiles_api import serilizers
from profiles_api import models
from profiles_api import permissions


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serilizer_class = serilizers.HelloSerilizers

    def list(self, request):
        """return a hello message"""
        a_viewset = [
            'Uses action (list, create, retrive, updatem, partioal_update',
            'Automaticly more functionality with less code',
            'provide more function with less code',
        ]
        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """create a new hello message"""
        serilizer = self.serilizer_class(data=request.data)
        if serilizer.is_valid():
            name = serilizer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serilizer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """handle getting an object by its id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """handle update an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """handle updating part of object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """handle removing an object"""
        return Response({'http_method': 'DELETE'})


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


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle create and update profile"""
    serializer_class = serilizers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwneProfils,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """handle create user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """handle create , reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serilizers.ProfileFeedItemSerializer
    queryset = models.ProgileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)














