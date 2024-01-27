from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField


class Tag(models.Model):
    class Meta:
        db_table = 'tags'

    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Map(models.Model):
    class Meta:
        db_table = 'maps'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    tags = models.ManyToManyField(Tag, blank=False)
    description = models.TextField(max_length=500, blank=True)

    # image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    class Meta:
        db_table = 'questions'

    title = models.CharField(max_length=255, blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('question', args=[self.id])


class Rating(models.Model):
    class Meta:
        db_table = 'ratings'

    profession = models.ForeignKey(Map, on_delete=models.CASCADE, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="ratings")
    rating = models.IntegerField(default=1, blank=True)
    position = models.IntegerField(default=1000, blank=True)
    public = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.profession}, {self.question}"


class Answer(models.Model):
    class Meta:
        db_table = 'comments'

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = RichTextField()
    public = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.author


class VideoAnswerLink(models.Model):
    class Meta:
        db_table = 'video_answer_links'

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    public = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class ExtraContentLink(models.Model):
    class Meta:
        db_table = 'extra_content_links'

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    url = models.URLField()
    public = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
