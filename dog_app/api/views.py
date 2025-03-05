from rest_framework.viewsets import ModelViewSet

from api.serializers import BreedSerializer, DogCreateSerializer, DogReadSerializer
from dogs.models import Breed, Dog


class DogViewSet(ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogReadSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "list":
            queryset = queryset.with_avg_age_by_breed()
        if self.action == "retrieve":
            queryset = queryset.get_with_count_dogs()
        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return super().get_serializer_class()
        return DogCreateSerializer


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.with_dog_count()
        return queryset
