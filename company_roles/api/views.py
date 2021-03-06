
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404

# import models and serializers
from .serializers import (
    RegistrationSerializer,
    LoginSerializer,
    UserListSerializer,
    UserInfoSerializer,
    RoleUpdateSerializer
)
from .models import User


class RegistrationView(viewsets.ViewSet):
    serializer_class = RegistrationSerializer
    permission_classes = (AllowAny, )

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User registration successful!',
                'user': {
                    'email': serializer.data['email']
                }
            }

            return Response(response, status=status_code)



class LoginView(viewsets.ViewSet):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny, )

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'Login successful',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                    'role': serializer.data['role']
                }
            }

            return Response(response, status=status_code)


class UserListView(viewsets.ViewSet):
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'uid'

    def list(self, request):
        current_user = request.user

        # only admins can view userlists
        if current_user.role != 1:
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You dont have enough permissions to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        else:
            users = User.objects.all()
            serializer = self.serializer_class(users, many=True, context={'request': request})
            response = {
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': 'Successfully fetched users',
                'users': serializer.data

            }
            return Response(response, status=status.HTTP_200_OK)

    def retrieve(self, request, uid=None):
        current_user = request.user

        # only admins can view user info
        if current_user.role != 1:
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You dont have enough permissions to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)

        users = User.objects.all()
        user = get_object_or_404(users, uid=uid)
        serializer = UserInfoSerializer(user,  context={'request': request})
        return Response(serializer.data)


    def update(self, request, uid=None):
        current_user = request.user

        # only admins can view user info
        if current_user.role != 1:
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You dont have enough permissions to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)


        users = User.objects.all()
        user = get_object_or_404(users, uid=uid)

        if user.role == 1:
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'User is admin, role cannot be changed at the moment'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)

        serializer = RoleUpdateSerializer(user, data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()

            users = User.objects.all()
            user = get_object_or_404(users, uid=uid)
            user_serializer = UserInfoSerializer(user,  context={'request': request})

            response = {
                'success': True,
                'statusCode': status.HTTP_200_OK,
                'message': 'User role updated',
                'updatedUser': user_serializer.data
            }

            return Response(response, status=status.HTTP_200_OK)
