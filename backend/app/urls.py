from django.urls import include, path
from rest_framework import routers

from app.views import AuthorViewSet
from app.views import ProfileView, DashboardView, OrderView, health_check


router = routers.DefaultRouter()
router.register(r"author", AuthorViewSet, basename="author")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("profile", ProfileView.as_view()),
    path("dashboard", DashboardView.as_view() ),
    path("order", OrderView.as_view()),
     path("health", health_check, name="health_check"),
]