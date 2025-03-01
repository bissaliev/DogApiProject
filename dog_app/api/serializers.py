from dogs.models import Breed, Dog
from rest_framework import serializers


class DogSerializer(serializers.ModelSerializer):
    avg_breed_age = serializers.IntegerField(read_only=True)
    count_breed_dogs = serializers.IntegerField(read_only=True)
    breed = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Dog
        fields = (
            "name",
            "age",
            "breed",
            "gender",
            "color",
            "favorite_food",
            "favorite_toy",
            "avg_breed_age",
            "count_breed_dogs",
        )


class BreedSerializer(serializers.ModelSerializer):
    count_dogs = serializers.IntegerField(read_only=True)

    class Meta:
        model = Breed
        fields = (
            "name",
            "size",
            "friendliness",
            "trainability",
            "shedding_amount",
            "exercise_needs",
            "count_dogs",
        )
