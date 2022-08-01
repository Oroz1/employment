from django.db import models
from core.models import TimeStampMixin
from company.models import Companies
from summary.models import Summaries, Occupations


class Hiring(TimeStampMixin):

    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'
        ordering = ('created_at', 'updated_at')

    company = models.ForeignKey(Companies, on_delete=models.CASCADE, verbose_name='компания')
    title = models.CharField(max_length=255, verbose_name='заголовок вакансии')
    tags = models.ManyToManyField('Tags', verbose_name='теги')
    salary = models.CharField(max_length=50, verbose_name='зарплата')
    occupation = models.ForeignKey(Occupations, on_delete=models.PROTECT, verbose_name='вид деятельности')
    description = models.TextField(verbose_name='описание')
    first_phone_number = models.CharField(max_length=13, verbose_name='номер телефона')
    second_phone_number = models.CharField(max_length=13, verbose_name='дополнительный номер телефона', blank=True, null=True)
    email = models.EmailField(verbose_name='почта', blank=True, null=True),
    responses = models.ManyToManyField(Summaries, verbose_name='отклики')

    def __str__(self):
        return f'{self.title}'


class Tags(TimeStampMixin):

    class Meta:
        verbose_name = 'тег для вакансии'
        verbose_name_plural = 'теги для вакансии'
        ordering = ('created_at', 'updated_at')

    title = models.CharField(max_length=100, verbose_name='название тега', unique=True)

    def __str__(self):
        return f'{self.title}'

# Create your models here.
