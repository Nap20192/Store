from django.http import HttpResponse
from rest_framework import generics
from .models import Product
from .serializer import ProductSerializer
import base64

def get_image_data_url(image_path):
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        return f"data:image/png;base64,{encoded_string}"
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        image_path = instance.image.path  # Путь к изображению на сервере
        image_data_url = get_image_data_url(image_path)
        if image_data_url:
            return HttpResponse(image_data_url)
        else:
            # Возвращаем 404 ошибку, если изображение не найдено
            return HttpResponse(status=404)
