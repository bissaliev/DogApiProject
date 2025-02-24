from django.db import models


class Breed(models.Model):
    """Модель пород собак"""

    class SizeChoices(models.TextChoices):
        TINY = "Tiny", "Tiny"
        SMALL = "Small", "Small"
        MEDIUM = "Medium", "Medium"
        LARGE = "Large", "Large"

    RATING_CHOICES = [(i, i) for i in range(1, 6)]

    name = models.CharField("название породы", max_length=255, db_index=True)
    size = models.CharField(
        "размер",
        choices=SizeChoices.choices,
        max_length=6,
        default=SizeChoices.MEDIUM,
    )
    friendliness = models.IntegerField("дружелюбность", choices=RATING_CHOICES)
    trainability = models.IntegerField("обучаемость", choices=RATING_CHOICES)
    shedding_amount = models.IntegerField(
        "уровень линьки", choices=RATING_CHOICES
    )
    exercise_needs = models.IntegerField(
        "потребность в активности", choices=RATING_CHOICES
    )

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"

    def __str__(self):
        return self.name


class Dog(models.Model):
    """Модель собак"""

    class GenderChoice(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"

    name = models.CharField("имя", max_length=255, db_index=True)
    age = models.IntegerField("возраст")
    breed = models.ForeignKey(
        "Breed",
        on_delete=models.CASCADE,
        related_name="dogs",
        verbose_name="порода",
    )
    gender = models.CharField(
        "пол",
        max_length=6,
        choices=GenderChoice.choices,
        default=GenderChoice.MALE,
    )
    color = models.CharField("окрас", max_length=50)
    favorite_food = models.CharField("любимая еда", max_length=255)
    favorite_toy = models.CharField("любимая игрушка", max_length=255)

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"

    def __str__(self):
        return self.name
