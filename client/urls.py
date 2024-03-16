from django.urls import path
from .views import ClientListCreateAPIView, ClientRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("clients/", ClientListCreateAPIView.as_view(), name="client-list-create"),
    path(
        "clients/<int:pk>/",
        ClientRetrieveUpdateDestroyAPIView.as_view(),
        name="client-detail",
    ),
]

from django.urls import path
from .views import (
    ClientListCreateAPIView,
    ClientRetrieveUpdateDestroyAPIView,
    ClientCreateAPIView,
)

urlpatterns = [
    path("clients/", ClientListCreateAPIView.as_view(), name="client-list-create"),
    path(
        "clients/<int:pk>/",
        ClientRetrieveUpdateDestroyAPIView.as_view(),
        name="client-detail",
    ),
    path("clients/register/", ClientCreateAPIView.as_view(), name="client-register"),
]


from django.urls import path
from .views import ClientListAPIView, ClientRetrieveAPIView

urlpatterns = [
    path("clients/", ClientListAPIView.as_view(), name="client-list"),
    path("clients/<int:pk>/", ClientRetrieveAPIView.as_view(), name="client-detail"),
]


urlpatterns = [
    path(
        "clients/<int:pk>/",
        ClientUpdateDestroyAPIView.as_view(),
        name="client-update-delete",
    ),
]

from django.urls import path
from .views import (
    ClientListCreateAPIView,
    ClientRetrieveUpdateDestroyAPIView,
    ClientCreateAPIView,
)

urlpatterns = [
    path("clients/", ClientListCreateAPIView.as_view(), name="client-list-create"),
    path(
        "clients/<int:pk>/",
        ClientRetrieveUpdateDestroyAPIView.as_view(),
        name="client-detail",
    ),
    path("clients/register/", ClientCreateAPIView.as_view(), name="client-register"),
]


urlpatterns = [
    path("clients/", ClientListCreateAPIView.as_view(), name="client-list-create"),
    path(
        "clients/<int:pk>/",
        ClientRetrieveUpdateDestroyAPIView.as_view(),
        name="client-detail",
    ),
    path("clients/register/", ClientCreateAPIView.as_view(), name="client-register"),
    path(
        "clients/<int:pk>/edit/",
        ClientUpdateDestroyAPIView.as_view(),
        name="client-update-delete",
    ),
]

from django.urls import path
from .views import (
    ClientListCreateAPIView,
    ClientRetrieveUpdateDestroyAPIView,
    ClientCreateAPIView,
    ClientUpdateDestroyAPIView,
)

urlpatterns = [
    path("clients/", ClientListCreateAPIView.as_view(), name="client-list-create"),
    path(
        "clients/<int:pk>/",
        ClientRetrieveUpdateDestroyAPIView.as_view(),
        name="client-detail",
    ),
    path("clients/register/", ClientCreateAPIView.as_view(), name="client-register"),
    path(
        "clients/<int:pk>/edit/",
        ClientUpdateDestroyAPIView.as_view(),
        name="client-update-delete",
    ),
]
