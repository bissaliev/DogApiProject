from rest_framework.viewsets import ModelViewSet

from api.serializers import BreedSerializer, DogCreateSerializer, DogReadSerializer
from dogs.models import Breed, Dog


class DogViewSet(ModelViewSet):
    """Вьюсет для модели Dog.

    Обрабатывает CRUD-операции для собак с использованием разных сериализаторов
    в зависимости от типа запроса. Поддерживает аннотации для списка и детального просмотра.
    """

    queryset = Dog.objects.all()
    serializer_class = DogReadSerializer

    def get_queryset(self):
        """Возвращает QuerySet с аннотациями в зависимости от действия.

        Для действия 'list' добавляет средний возраст породы, для 'retrieve' — количество собак
        той же породы.

        Returns:
            QuerySet: QuerySet с соответствующими аннотациями.
        """

        queryset = super().get_queryset()
        if self.action == "list":
            queryset = queryset.with_avg_age_by_breed()
        if self.action == "retrieve":
            queryset = queryset.get_with_count_dogs()
        return queryset

    def get_serializer_class(self):
        """Определяет класс сериализатора в зависимости от метода запроса.

        Использует DogReadSerializer для GET-запросов и DogCreateSerializer для остальных.

        Returns:
            type: Класс сериализатора для текущего запроса.
        """

        if self.request.method == "GET":
            return super().get_serializer_class()
        return DogCreateSerializer


class BreedViewSet(ModelViewSet):
    """Вьюсет для модели Breed.

    Обрабатывает CRUD-операции для пород собак с аннотацией количества связанных собак.
    """

    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

    def get_queryset(self):
        """Возвращает QuerySet с аннотацией количества собак.

        Returns:
            QuerySet: QuerySet с аннотацией count_dogs для каждой породы.
        """

        return super().get_queryset().with_dog_count()
