from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from .models import User
from .serializers import UserSerializer
from core.permissions import IsAccountOwnerOrReadOnly

class Signup(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = ()

    def post(self, request:Request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message":"successful",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        response = {
            "message":"failed",
            "info": serializer.errors
        }
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

# class Login(APIView):
#     permission_classes = ()
#     def post(self, request:Request):
#         email = request.data.get("email")
#         password = request.data.get("password")

#         user = authenticate(email=email, password=password)

#         if user is not None:
#             response = {
#                 "message":"successful",
#                 'data': {
#                     'user':str(user),
#                     'token': user.auth_token.key
#                 }
#             }
#             return Response(data=response, status=status.HTTP_200_OK)
#         response = {
#             "message":"failed",
#             "info": "user not found. Check credentials"
#         }
#         return Response(data=response, status=status.HTTP_404_NOT_FOUND)

class RetrieveUpdateDeleteUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAccountOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
    