from django.db import models

# Create your models here.
from autho.models import User


class BookJournalBase(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField(default=1)
    genre = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Journal(BookJournalBase):
    BULLET = 'BULLET'
    FOOD = 'FOOD'
    TRAVEL = 'TRAVEL'
    SPORT = 'SPORT'
    types = (
        (BULLET, BULLET),
        (FOOD, FOOD),
        (TRAVEL, TRAVEL),
        (SPORT, SPORT)
    )
    type = models.CharField(
        choices=types,
        max_length=100
    )
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journals')

    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'



