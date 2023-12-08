from rest_framework import viewsets
from catalog.serializers import CategorySerializer
from catalog.models import Category


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
