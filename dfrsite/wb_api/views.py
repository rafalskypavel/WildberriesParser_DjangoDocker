# views.py
import time

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .tasks import fetch_product_task
from .models import Product
from .serializer import ProductSerializer
import logging

logger = logging.getLogger(__name__)

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateAPIView(APIView):
    """
    Представление для создания нового продукта (POST запрос).
    """
    def post(self, request):
        article = self.get_article(request)
        if not article:
            return Response({'error': 'Article is required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            task = fetch_product_task.delay(article)
            return Response({'task_id': task.id}, status=status.HTTP_202_ACCEPTED)

        except Exception as e:
            logger.error(f'Error while starting product fetch task: {str(e)}')
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_article(self, request) -> int:
        article = request.data.get('article')

        # Проверка на наличие значения
        if article is None:
            raise ValueError("Article is required.")

        # Проверка, что значение состоит только из цифр
        if not article.isdigit():
            raise ValueError("Article must be a numeric value.")

        # Преобразуем строку в целое число
        article_int = int(article)

        # Проверка длины значения
        if not (5 <= len(article) <= 15):
            raise ValueError("Article length must be between 5 and 15 characters.")

        return article_int


class ProductFormView(APIView):
    """
    Представление для отображения страницы с формами для GET и POST запросов.
    """
    def get(self, request):
        return render(request, 'product_form.html')
