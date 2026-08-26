from django.urls import include, path
from rest_framework import routers

from app import views
from app.profile_view import ProfileView

router = routers.DefaultRouter()
router.register(r"author", views.AuthorViewSet, basename="author")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("profile", ProfileView.as_view()),
]