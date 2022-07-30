from core.models import Users , TimeStampMixin
from django.db import models


class Summaries(TimeStampMixin):

    MALE = 'M'
    FEMALE = 'F'

    GENDER = (
        (MALE, 'Мужской',),
        (FEMALE, 'Женский',),
    )

    class Meta:
        verbose_name = 'резюме'
        verbose_name_plural = 'резюме'
        ordering = ('created_at', 'updated_at')

    user = models.OneToOneField(Users, on_delete=models.CASCADE, verbose_name='пользователь')
    first_name = models.CharField(max_length=30, verbose_name='имя')
    surname = models.CharField(max_length=30, verbose_name='фамилия')
    phone_number = models.CharField(max_length=13, verbose_name='номер телефона')
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True, verbose_name='город проживания')
    date_of_birth = models.DateField(verbose_name='день рождения')
    gender = models.CharField(max_length=1, verbose_name='пол', choices=GENDER, default=MALE)
    citizenship = models.ForeignKey('Citizenship', on_delete=models.SET_NULL, null=True, verbose_name='гражданство')
    dream_work = models.CharField(max_length=70, verbose_name='желаемая должность')
    salary = models.IntegerField(verbose_name='желаемая зарплата')
    place_of_work = models.CharField(max_length=100, blank=True, null=True, verbose_name='место работы')
    key_skills = models.ManyToManyField('Skills', verbose_name='навыки')
    education = models.ForeignKey('Education', on_delete=models.CASCADE, verbose_name='образование')
    language = models.CharField(max_length=50, verbose_name='родной язык')
    foreign_language = models.ManyToManyField('Foreign_language', verbose_name='иностранные языки')
    
    hasWorkExperience = models.BooleanField(verbose_name='опыт работы')
    #else:
        # без опыта работы 
    с = models.CharField(max_length=250, blank=True, null=True, verbose_name='почему нету опыта работы причина:')
    
    


#города 
class City(TimeStampMixin):
    name = models.CharField(max_length=50, verbose_name='город')

#страны
class Citizenship(TimeStampMixin):
    name = models.CharField(max_length=70, verbose_name='страна гражданство')
#навыки
class Skills(TimeStampMixin):
    name = models.CharField(max_length=50, verbose_name='навыки')
#образование
class Education(TimeStampMixin):
    name = models.CharField(max_length=40, verbose_name='образование')
#иностранных языка
class Foreign_language(TimeStampMixin):
    name = models.CharField(max_length=40, verbose_name='имена иностранных языка')
