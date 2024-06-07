from django.urls import path
from .views import AddAlbumView, EditAlbumView, DeleteAlbumView

urlpatterns = [
    path('add/', AddAlbumView.as_view(), name='add_album'),
    path('edit/<int:id>/', EditAlbumView.as_view(), name='edit_album'),
    path('delete/<int:id>/', DeleteAlbumView.as_view(), name='delete_album'),
]