from django.contrib import admin

from . import models
from .models import Rating, Question, Map, Answer, VideoAnswerLink, ExtraContentLink


def make_public(modeladmin, request, queryset):
    queryset.update(public=True)


admin.site.register(models.Tag)


@admin.register(ExtraContentLink)
class ExtraContentLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'title', 'public', 'created_at')


@admin.register(VideoAnswerLink)
class VideoAnswerLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'title', 'public', 'created_at')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'public', 'created_at')
    actions = [make_public]


@admin.register(Map)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'profession', 'rating', 'position', 'public', 'created_at')
    search_fields = ('question__title',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tag')
    search_fields = ('title',)
