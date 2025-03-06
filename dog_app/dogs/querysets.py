from django.db.models import Avg, Count, QuerySet


class DogQueryset(QuerySet):
    """Кастомный QuerySet для модели Dog"""

    def get_with_count_dogs(self) -> QuerySet:
        """Добавляет количество собак той же породы для каждой собаки.

        Returns:
            Queryset: QuerySet с аннотацией count_breed_dogs, содержащей
            количество собак той же породы.
        """
        return self.annotate(count_breed_dogs=Count("breed__dogs"))

    def with_avg_age_by_breed(self) -> QuerySet:
        """Добавляет средний возраст собак для каждой породы к списку собак.

        Returns:
            Queryset: QuerySet с аннотацией avg_breed_age, содержащей
            средний возраст собак той же породы.
        """
        return self.annotate(avg_breed_age=Avg("breed__dogs__age"))


class BreedQuerySet(QuerySet):
    """Кастомный QuerySet для модели Breed"""

    def with_dog_count(self) -> QuerySet:
        """Добавляет количество собак для каждой породы

        Returns:
            Queryset: QuerySet с аннотацией count_dogs, содержащей
            количество собак той же породы.
        """
        return self.annotate(count_dogs=Count("dogs"))
