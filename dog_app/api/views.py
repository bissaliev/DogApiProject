from api.serializers import BreedSerializer, DogSerializer
from django.db.models import Avg, Count
from dogs.models import Breed, Dog
from rest_framework.viewsets import ModelViewSet


class DogViewSet(ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action == "list":
            queryset = queryset.annotate(avg_breed_age=Avg("breed__dogs__age"))
        if self.action == "retrieve":
            queryset = queryset.annotate(
                count_breed_dogs=Count("breed__dogs__id")
            )
        return queryset


class BreedViewSet(ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(count_dogs=Count("dogs"))
        return queryset
