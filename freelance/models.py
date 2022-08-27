from django.db import models
from core.models import TimeStampMixin, Users
from hiring.models import Tags
from summary.models import Summaries, CURRENCY


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
    reword = models.CharField(max_length=30, verbose_name='оплата')
    status = models.CharField(verbose_name='статус', max_length=10, choices=STATUS_OF_ORDERS, default=TOPICAL)
    currency = models.CharField(max_length=3, verbose_name='валюта зарплаты', choices=CURRENCY)
    maker = models.OneToOneField(Users, related_name='freelance', blank=True, null=True, on_delete=models.SET_NULL, verbose_name='выполняющий')
    responses = models.ManyToManyField(Summaries, verbose_name='отклики', blank=True)

    def __str__(self):
        return f'{self.title}'
    
    @property
    def get_full_name(self):
        if self.owner is not None:
            return f'{self.owner.last_name} {self.owner.first_name}'
        return self.owner
 
# Create your models here.
