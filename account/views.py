from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .serializers import RegisterUserSerializer
from .models import User

# User = get_object_or_404

class RegisterUserView(APIView):
    @swagger_auto_schema(request_body=RegisterUserSerializer())
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('vy uspeshno zaregistrirovalis', status=200)

    # @api_view(['POST'])
    # def register_user(request):
    #   serializer = RegisterUserSerializer(data=request.data)
    #   serializer.is_valid(raise_exception=True)
    #   serializer.save()
    #   return Response("Вы успешно зарегистрировались", status=201)

class DeleteUserView(APIView):
    def delete(self, request, email):
        user = get_object_or_404(User, email=email)
        if user.is_staff:
            return Response(status=403) # zapreshaem
        user.delete()
        return Response(status=204)

    # @api_view(['DELETE'])
    # def delete_user(request, email):
    #     user = get_object_or_404(User, email=email)
    #     if user.is_staff:
    #         return Response(status=403) # zapreshaem
    #     user.delete()
    #     return Response(status=204)



























