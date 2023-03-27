from django.db import models
from django.urls import reverse


class News1(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f'{self.title.title ()}: {self.content[:100]}'

    def get_absolute_url(self) :
        return reverse('news_detail', args=[str(self.id)])

