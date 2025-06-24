from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100)

class Note(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)

class Perfume(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.PROTECT)
    notes = models.ManyToManyField(Note, through='PerfumeNote')

class PerfumeNote(models.Model):
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    intensity = models.PositiveSmallIntegerField(default=1)

    class Meta:
        unique_together = ('perfume', 'note')
