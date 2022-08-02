from django.db import models
from core.models import TimeStampMixin, Users
from hiring.models import Tags
from summary.models import Summaries


TOPICAL = 'topical'

STATUS_OF_ORDERS = (
    (TOPICAL, 'Актуальное'),
    ('accepted', 'Принитое'),
    ('finished', 'Завершенное'),
)


class Orders(TimeStampMixin):

    class Meta:
        verbose_name = 'фриланс заказ'
        verbose_name_plural = 'фриланс заказы'
        ordering = ('created_at', 'updated_at')

    owner = models.OneToOneField(Users, on_delete=models.CASCADE, verbose_name='заказчик')
    title = models.CharField(max_length=120, verbose_name='заголовок заказа')
    description = models.CharField(max_length=1500, verbose_name='описание')
    tags = models.ManyToManyField(Tags, verbose_name='теги')
    first_phone_number = models.CharField(max_length=13, verbose_name='номер телефона')
    second_phone_number = models.CharField(max_length=13, verbose_name='дополнительный номер телефона', blank=True, null=True)
    email = models.EmailField(verbose_name='почта', blank=True, null=True),
    status = models.CharField(verbose_name='статус', max_length=10, choices=STATUS_OF_ORDERS, default=TOPICAL)
    maker = models.OneToOneField(Users, related_name='freelance', blank=True, null=True, on_delete=models.SET_NULL, verbose_name='выполняющий')
    responses = models.ManyToManyField(Summaries, verbose_name='отклики')

    def __str__(self):
        return f'{self.title}'

# Create your models here.
