from django.db import models

# Create your models here.
from django.db import models

class Quote(models.Model): #quote наследуется от models.Model
    text = models.TextField(unique=True)  #текст цитаты, уникальный
    source = models.CharField(max_length=255)  #источник (фильм, книга и пр)
    weight = models.PositiveIntegerField(default=1)  # вес
    likes = models.PositiveIntegerField(default=0)  #количество лайков
    dislikes = models.PositiveIntegerField(default=0)  #количество дизлайков
    views = models.PositiveIntegerField(default=0)  #количество просмотров

    def __str__(self):
        return f"{self.text[:30]}... ({self.source})"
