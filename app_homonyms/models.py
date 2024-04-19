from django.db import models


class WordType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Word Types'
        db_table = 'word_types'




class Homonyms(models.Model):
    word = models.CharField(max_length=100, null=False, blank=False)
    origin = models.CharField(max_length=100, null=True, blank=True)
    word_type = models.ForeignKey(WordType, on_delete=models.CASCADE)
    meaning = models.CharField(max_length=100, null=False, blank=False)
    example = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name_plural = 'Homonyms'
        db_table = 'homonyms'
        ordering = ['id']