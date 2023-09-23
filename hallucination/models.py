from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Vision(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    artist = models.CharField(max_length=200)
    composer = models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Sight(models.Model):
    title = models.CharField(max_length=12)
    vision = models.ForeignKey(Vision, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/%vision_title/', blank=True, null=True)
    priority = models.IntegerField()
    midi = models.IntegerField()
    command = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    def vision_title(self):
        return self.vision.title
    
    class Meta:
        ordering = ["priority"]