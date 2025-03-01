from api.views import BreedViewSet, DogViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = "api"


router = DefaultRouter()


router.register("dogs", DogViewSet, basename="dogs")
router.register("breeds", BreedViewSet, basename="breeds")


urlpatterns = [path("", include(router.urls))]
