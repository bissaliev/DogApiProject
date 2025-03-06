from django.db import models

from dogs.querysets import BreedQuerySet, DogQueryset


class Breed(models.Model):
    """Модель пород собак

    Attributes:
        name (str): Название породы.
        size (str): Размер породы (Tiny, Small, Medium, Large).
        friendliness (int): Уровень дружелюбия (1-5).
        trainability (int): Уровень обучаемости (1-5).
        shedding_amount (int): Уровень линьки (1-5).
        exercise_needs (int): Уровень активности (1-5).
    """

    class SizeChoices(models.TextChoices):
        TINY = "Tiny", "Tiny"
        SMALL = "Small", "Small"
        MEDIUM = "Medium", "Medium"
        LARGE = "Large", "Large"

    RATING_CHOICES = [(i, i) for i in range(1, 6)]

    name = models.CharField("название породы", max_length=255, unique=True)
    size = models.CharField("размер", choices=SizeChoices.choices, max_length=6, default=SizeChoices.MEDIUM)
    friendliness = models.PositiveSmallIntegerField("дружелюбность", choices=RATING_CHOICES)
    trainability = models.PositiveSmallIntegerField("обучаемость", choices=RATING_CHOICES)
    shedding_amount = models.PositiveSmallIntegerField("уровень линьки", choices=RATING_CHOICES)
    exercise_needs = models.PositiveSmallIntegerField("потребность в активности", choices=RATING_CHOICES)

    objects = BreedQuerySet.as_manager()

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"

    def __str__(self):
        return self.name


class Dog(models.Model):
    """Модель собак

    Attributes:
        name (str): Имя собаки.
        age (int): Возраст собаки в годах.
        breed (Breed): Порода собаки (внешний ключ на модель Breed).
        gender (str): Пол собаки (Male,Female).
        color (str): Окрас собаки.
        favorite_food (str): Любимая еда собаки.
        favorite_toy (str): Любимая игрушка собаки.
    """

    class GenderChoice(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"

    name = models.CharField("имя", max_length=255, db_index=True)
    age = models.PositiveIntegerField("возраст")
    breed = models.ForeignKey("Breed", on_delete=models.CASCADE, related_name="dogs", verbose_name="порода")
    gender = models.CharField("пол", max_length=6, choices=GenderChoice.choices, default=GenderChoice.MALE)
    color = models.CharField("окрас", max_length=50)
    favorite_food = models.CharField("любимая еда", max_length=255)
    favorite_toy = models.CharField("любимая игрушка", max_length=255)

    objects = DogQueryset.as_manager()

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"

    def __str__(self):
        return self.name
