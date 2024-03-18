from django.urls import path
from .views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView, UserCreateAPIView


urlpatterns = [
    path("users/", UserListCreateAPIView.as_view(), name="user-list-create"),
    path(
        "users/<int:pk>/",
        UserRetrieveUpdateDestroyAPIView.as_view(),
        name="user-detail",
    ),
]

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path('users/register/', UserCreateAPIView.as_view(), name='user-register'),
]

