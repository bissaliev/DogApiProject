from rest_framework.viewsets import ModelViewSet

from api.serializers import BreedSerializer, DogSerializer
from dogs.models import Breed, Dog


class DogViewSet(ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "list":
            queryset = queryset.with_avg_age_by_breed()
        if self.action == "retrieve":
            queryset = queryset.get_with_count_dogs()
        return queryset


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.with_dog_count()
        return queryset
