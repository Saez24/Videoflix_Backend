from django.urls import path
from .views import ProfileViewSets, ProfileAdultViewSets, ProfileChildViewSets, ProfileListView, ProfileDetailView

urlpatterns = [
    path('profile/', ProfileListView.as_view(), name='profile-list'),  # Alle Profile abrufen
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),  # Einzelnes Profil abrufen/bearbeiten
    path('adult/', ProfileAdultViewSets.as_view(), name='adult-list'),
    path('child/', ProfileChildViewSets.as_view(), name='child-list'),
    path('', ProfileDetailView.as_view(), name='profile-me'),
]

