from .models import Client, Driver
from .serializers import ClientSerializer, DriverSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response

from django.contrib.auth.models import User
from rest_auth.registration.views import RegisterView

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class CustomClientRegisterView(RegisterView):
    queryset = Client.objects.all()

class ClientAPIView(APIView):
    @staticmethod
    def get(request):
        clients = User.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)


class GenericClientAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ClientSerializer
    queryset = User.objects.all()

    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)




# Driver Views

class CustomDriverRegisterView(RegisterView):
    queryset = Driver.objects.all()

class DriverAPIView(APIView):
    @staticmethod
    def get(request):
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data)


class GenericDriverAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)