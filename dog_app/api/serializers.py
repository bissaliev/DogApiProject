from rest_framework import serializers

from dogs.models import Breed, Dog


class DogCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания и изменения объектов модели Dog"""

    class Meta:
        model = Dog
        fields = (
            "id",
            "name",
            "age",
            "breed",
            "gender",
            "color",
            "favorite_food",
            "favorite_toy",
        )


class DogReadSerializer(serializers.ModelSerializer):
    """Сериализатор для чтения объектов модели Dog"""

    avg_breed_age = serializers.IntegerField(read_only=True)
    count_breed_dogs = serializers.IntegerField(read_only=True)
    breed = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Dog
        fields = (
            "id",
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
    """Сериализатор для модели Breed"""

    count_dogs = serializers.IntegerField(read_only=True)

    class Meta:
        model = Breed
        fields = (
            "id",
            "name",
            "size",
            "friendliness",
            "trainability",
            "shedding_amount",
            "exercise_needs",
            "count_dogs",
        )
