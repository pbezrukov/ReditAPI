from rest_framework import status
# from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# from .models import User
# from .serializers import LoginSerializer
from .serializers import RegistrationSerializer


class RegistrationAPIView(APIView):

    serializer_class = RegistrationSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            status=status.HTTP_201_CREATED,
        )
