from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework import mixins, views
from rest_framework.throttling import UserRateThrottle
from rest_framework import serializers
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class OncePerDayUserThrottle(UserRateThrottle):
    rate = '1/day'


@api_view(('GET',))
def get_routes(request):
    routes = {'routes': [
        {
            'method': 'GET',
            'url': '/v1/todos/',
            'permissions': ['authenticated']
        },
        {
            'method': 'GET',
            'url': '/v1/todos/<int:pk>/',
            'permissions': ['authenticated', 'creator']
        },
        {
            'method': 'POST',
            'url': '/v1/todos/create/',
            'permissions': ['authenticated']
        },
        {
            'method': 'PUT',
            'url': '/v1/todos/<int:pk>/update/',
            'permissions': ['authenticated', 'creator']
        },
        {
            'method': 'DELETE',
            'url': '/v1/todos/<int:pk>/delete/',
            'permissions': ['authenticated', 'creator']
        }
    ]}
    return Response(routes)


# raise serializers.ValidationError(f"Hello is not allowed.")

class TodoMixinList(mixins.ListModelMixin, GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # throttle_classes = [OncePerDayUserThrottle]

    def get(self, request, *arg, **kwargs):
        print(request)
        return self.list(request, *arg, **kwargs)
        return self.list_done(request, *arg, **kwargs)

    def get_queryset(self, *args, **kwargs):
        return Todo.objects.filter(user=self.request.user)

    def list_done(self, request, *args, **kwargs):
        queryset = Todo.objects.filter(done=True)
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)


class TodoMixinCreate(mixins.CreateModelMixin, GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # throttle_classes = [OncePerDayUserThrottle]

    def post(self, request, *args, **kwargs):
        print('created - 1')
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        print("created - 2")
        serializer.save(user=self.request.user)


class TodoMixinUpdate(mixins.UpdateModelMixin, GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]

    # throttle_classes = [OncePerDayUserThrottle]

    def put(self, request, *args, **kwargs):
        title = request.data.get('title')
        print(title)
        print(request.data)
        if title:
            return self.update(request, *args, **kwargs)  # full data update
        return self.partial_update(request, *args, **kwargs)  # partial data update

    def perform_update(self, serializer):
        print("next")
        # send_email
        serializer.save()


class TodoMixinRetrieve(mixins.RetrieveModelMixin, GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, JWTAuthentication]
    permission_classes = [IsOwner]
    lookup_field = 'pk'

    # throttle_classes = [OncePerDayUserThrottle]

    def get(self, request, *args, **kwargs):
        print(kwargs['pk'])
        return self.retrieve(request, *args, **kwargs)


class TodoMixinDestroy(mixins.DestroyModelMixin, GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, JWTAuthentication]
    permission_classes = [IsOwner]
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
