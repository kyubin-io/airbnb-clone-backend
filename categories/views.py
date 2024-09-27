from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySerializer

class Categories(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()