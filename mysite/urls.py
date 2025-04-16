from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse

def home_view(request):
    return JsonResponse({"message": "Bienvenido a la API de la Cafetería"})

urlpatterns = [
    path('', home_view),
    path('admin/', admin.site.urls),
    path('api/products/', include('products.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
