from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from autho.serializers import SignUpSerializer, UserSerializer, SignInSerializer
from autho.utils import create_token


class AuthViewSet(viewsets.GenericViewSet,):

    def get_permissions(self):
        if self.action == 'sign_out':
            return (IsAuthenticated(),)
        return ()

    def get_serializer_class(self):
        if self.action == 'sign_up':
            return SignUpSerializer
        elif self.action == 'sign_in':
            return SignInSerializer
        return None

    def sign_up(self, request, *args, **kwargs):
        from autho.services import create_user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user(serializer.validated_data)
        token = create_token(user)
        return Response(UserSerializer({'user': user, 'token': token}).data)

    def sign_in(self, request, *args, **kwargs):
        from autho.utils import authorize
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = authorize(request, **serializer.validated_data)
        return Response(UserSerializer({'user': user, 'token': token}).data)

    def sign_out(self, request, *args, **kwargs):
        from utils import logout
        logout(self.request)
        return Response()
