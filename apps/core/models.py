from django.db import models
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    def image_path(self, filename):
        return 'news/{}/'.format(filename)

    title=models.CharField(max_length=100)
    text=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    news_thumbnail = ProcessedImageField(
        upload_to=image_path,
        processors=[ResizeToFill(319, 200)],
        format='JPEG',
        options={'quality': 80},
        blank=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"

    def __str__(self):
        return self.title
    


class Band(models.Model):
    def image_path(self, filename):
        return 'band/{}'.format(filename)

    name=models.CharField(max_length=200)
    function=models.CharField(max_length=200)
    birth_date=models.DateField()
    description=models.TextField()
    active=models.BooleanField()
    avatar_thumbnail = ProcessedImageField(
        upload_to=image_path,
        processors=[ResizeToFill(200, 200)],
        format='JPEG',
        options={'quality': 80},
        blank=True
    )

    class Meta:
        verbose_name = "Banda"
        verbose_name_plural = "Banda"

    def __str__(self):
        return self.name


class Concert(models.Model):
    def image_path(self, filename):
        return 'cartazes/{}/{}/{}/{}'.format(self.date.year,self.date.month,self.date.day,filename)

    title=models.CharField(max_length=200)
    local=models.CharField(max_length=200)
    date=models.DateField()
    localization=models.CharField(max_length=400)
    cartaz_thumbnail = ProcessedImageField(
        upload_to=image_path,
        processors=[ResizeToFill(350, 496)],
        format='JPEG',
        options={'quality': 80},
        blank=True
    )

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agenda"

    def __str__(self):
        return "{}-{}".format(self.title, self.date)


class Video(models.Model):
    title=models.CharField(max_length=200)
    url=models.URLField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Vídeos"

    def __str__(self):
        return self.title
    