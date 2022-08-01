from django.db import models
from core.models import TimeStampMixin
from core.models import Users


class Companies(TimeStampMixin):
    
    class Meta:
        verbose_name = 'компания'
        verbose_name_plural = 'компании'
        ordering = ('created_at', 'updated_at')

    logo = models.ImageField(upload_to='logo_companies/', verbose_name='логотип компании')
    title = models.CharField(max_length=70, blank=True, null=True, verbose_name='название компании')
    information = models.CharField(max_length=250, blank=True, null=True, verbose_name='информация')
    owner = models.OneToOneField(Users, on_delete=models.SET_NULL, null=True, verbose_name='владелец')

    def __str__(self):
        return f'{self.title}'
# Create your models here.
