from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import SendEmailSerializer
from .services import _calculate_number_products


class SendEmailView(CreateAPIView):
    """Работа с отправкой письма покупателю."""
    def post(self, request, *args, **kwargs):
        serializer = SendEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        _calculate_number_products(serializer.data.get('products'))
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

