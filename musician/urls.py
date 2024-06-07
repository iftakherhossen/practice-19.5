from django.urls import path
from .views import AddMusicianView, EditMusicianView, DeleteMusicianView

urlpatterns = [
    path('add/', AddMusicianView.as_view(), name='add_musician'),
    path('edit/<int:id>/', EditMusicianView.as_view(), name='edit_musician'),
    path('delete/<int:id>/', DeleteMusicianView.as_view(), name='delete_musician'),
]