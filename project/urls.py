# from django.urls import path
# from .views import ProjectListCreateAPIView, ProjectRetrieveUpdateDestroyAPIView

from django.urls import path
from .views import (
    ProjectListCreateAPIView,
    ProjectRetrieveUpdateDestroyAPIView,
    UserProjectsAPIView,
)

urlpatterns = [
    path("projects/", ProjectListCreateAPIView.as_view(), name="project-list-create"),
    path(
        "projects/<int:pk>/",
        ProjectRetrieveUpdateDestroyAPIView.as_view(),
        name="project-detail",
    ),
]


urlpatterns = [
    path("projects/", ProjectListCreateAPIView.as_view(), name="project-list-create"),
    path(
        "projects/<int:pk>/",
        ProjectRetrieveUpdateDestroyAPIView.as_view(),
        name="project-detail",
    ),
    path("user/projects/", UserProjectsAPIView.as_view(), name="user-projects"),
]

# project/urls.py

from django.urls import path
from .views import (
    ProjectListCreateAPIView,
    ProjectRetrieveUpdateDestroyAPIView,
    UserProjectsAPIView,
)

urlpatterns = [
    path("projects/", ProjectListCreateAPIView.as_view(), name="project-list-create"),
    path(
        "projects/<int:pk>/",
        ProjectRetrieveUpdateDestroyAPIView.as_view(),
        name="project-detail",
    ),
    path("user/projects/", UserProjectsAPIView.as_view(), name="user-projects"),
]

urlpatterns = [
    path("projects/", ProjectListCreateAPIView.as_view(), name="project-list-create"),
    path(
        "projects/<int:pk>/",
        ProjectRetrieveUpdateDestroyAPIView.as_view(),
        name="project-detail",
    ),
    path("user/projects/", UserProjectsAPIView.as_view(), name="user-projects"),
    path(
        "projects/<int:pk>/edit/",
        ProjectUpdateDestroyAPIView.as_view(),
        name="project-update-delete",
    ),
]

from django.urls import path
from .views import (
    ProjectListCreateAPIView,
    ProjectRetrieveUpdateDestroyAPIView,
    UserProjectsAPIView,
    ProjectUpdateDestroyAPIView,
)

urlpatterns = [
    path("projects/", ProjectListCreateAPIView.as_view(), name="project-list-create"),
    path(
        "projects/<int:pk>/",
        ProjectRetrieveUpdateDestroyAPIView.as_view(),
        name="project-detail",
    ),
    path("user/projects/", UserProjectsAPIView.as_view(), name="user-projects"),
    path(
        "projects/<int:pk>/edit/",
        ProjectUpdateDestroyAPIView.as_view(),
        name="project-update-delete",
    ),
]
