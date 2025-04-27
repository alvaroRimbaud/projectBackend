from django.urls import path
from .views import UserRegisterView, UserListView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('listar/', UserListView.as_view(), name='user-list'),
    path('registro/', UserRegisterView.as_view(), name='user-register'),
    path('actualizar/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('eliminar/<int:pk>/', UserDeleteView.as_view(), name='user-delete')
]
