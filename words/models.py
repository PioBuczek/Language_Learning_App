from django.db import models


class WordGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Word(models.Model):
    word = models.CharField(
        max_length=100,
    )
    translation = models.CharField(max_length=100)
    group = models.ForeignKey(
        WordGroup, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.word} - {self.translation}"
