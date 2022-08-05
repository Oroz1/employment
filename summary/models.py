from core.models import Users , TimeStampMixin, GENDER, MALE
from django.db import models


CITIES = (
    ('aidarken', 'Айдаркен'),
    ('baetov', 'Баетов'),
    ('balykchy', 'Балыкчы'),
    ('batken', 'Баткен'),
    ('bishkek', 'Бишкек'),
    ('jalal-abad', 'Джалал-Абад'),
    ('isfana', 'Исфана'),
    ('kadamjai', 'Кадамжай'),
    ('kaindy', 'Каинды'),
    ('kant', 'Кант'),
    ('kara-balta', 'Кара-Балта'),
    ('karkol', 'Каракол'),
    ('kara-kul', 'Кара-Куль'),
    ('kara-suu', 'Кара-Суу'),
    ('kemin', 'Кемин'),
    ('kerben', 'Кербен'),
    ('kok-jongag', 'Кок-Джангак'),
    ('kochkor-ata', 'Кочкор-Ата'),
    ('kyzyl-kiya', 'Кызыл-Кия'),
    ('mailuu-suu', 'Майлуу-Суу'),
    ('naryn', 'Нарын'),
    ('nookat', 'Ноокат'),
    ('orlovka', 'Орловка'),
    ('osh', 'Ош'),
    ('rybache', 'Рыбачье'),
    ('sulukty', 'Сулюкта'),
    ('talas', 'Талас'),
    ('tash-kumyr', 'Таш-Кумыр'),
    ('tokmak', 'Токмак'),
    ('toktogul', 'Токтогул'),
    ('uzgen', 'Узген'),
    ('cholpon-ata', 'Чолпон-Ата'),
    ('shopokov', 'Шопоков'),
)

EUDCATION_LEVELS = (
    ('secondary', 'Среднее'),
    ('special_secondary', 'Среднее специальное'),
    ('unfinished_higher', 'Неоконченное высшее'),
    ('higher', 'Высшее'),
    ('bachelor', 'Бакалавр'),
    ('master', 'Магистр'),
    ('candidate', 'Кандидат наук'),
    ('doctor', 'Доктор наук'),
)

CURRENCY = (
    ('KGS', 'KGS'),
    ('USD', 'USD'),
    ('EUR', 'EUR'),
)


class Summaries(TimeStampMixin):

    class Meta:
        verbose_name = 'резюме'
        verbose_name_plural = 'резюме'
        ordering = ('created_at', 'updated_at')

    user = models.OneToOneField(Users, on_delete=models.CASCADE, verbose_name='пользователь')
    first_name = models.CharField(max_length=30, verbose_name='имя')
    surname = models.CharField(max_length=30, verbose_name='фамилия')
    phone_number = models.CharField(max_length=13, verbose_name='номер телефона')
    city = models.CharField(max_length=50, verbose_name='город проживания', choices=CITIES)
    date_of_birth = models.DateField(verbose_name='день рождения')
    gender = models.CharField(max_length=1, verbose_name='пол', choices=GENDER, default=MALE)
    citizenship = models.ForeignKey('Citizenships', on_delete=models.SET_NULL, null=True, verbose_name='гражданство')
    dream_work = models.CharField(max_length=70, verbose_name='желаемая должность')
    occupations = models.ManyToManyField('Occupations', verbose_name='Род деятельности')
    salary = models.IntegerField(verbose_name='желаемая зарплата')
    currency = models.CharField(max_length=3, verbose_name='валюта зарплата', choices=CURRENCY)
    key_skills = models.ManyToManyField('Skills', verbose_name='навыки')
    education = models.ManyToManyField('Education', verbose_name='образование')
    language = models.ForeignKey('ForeignLanguages', verbose_name='родной язык', on_delete=models.SET_NULL, null=True, related_name='summaries_native')
    foreign_language = models.ManyToManyField('ForeignLanguages', verbose_name='иностранные языки', related_name='summaries_foreign')
    isMoving = models.BooleanField(default=False, verbose_name='переезд')
    isDistantWork = models.BooleanField(default=False, verbose_name='удалённая работа')
    job_experience = models.ManyToManyField('JobExperience', verbose_name='предыдущие работы')

    def __str__(self):
        return f'{self.user.name}'
 
    

class Occupations(TimeStampMixin):
    
    class Meta:
        verbose_name = 'профессия'
        verbose_name_plural = 'профессии'
        ordering = ('created_at', 'updated_at')

    title = models.CharField(max_length=60, verbose_name='название профессии', unique=True)
    is_main = models.BooleanField(default=False, verbose_name='основной', blank=True)
    attributes = models.ManyToManyField('self', verbose_name='атрибуты')

    def __str__(self):
        return f'{self.title}'
    

class Citizenships(TimeStampMixin):

    class Meta:
        verbose_name = 'гражданство'
        verbose_name_plural = 'гражданства'
        ordering = ('created_at', 'updated_at')

    title = models.CharField(max_length=70, verbose_name='страна гражданство', unique=True)
    
    def __str__(self):
        return f'{self.title}'



class Skills(TimeStampMixin):

    class Meta:
        verbose_name = 'навык'
        verbose_name_plural = 'навыки'
        ordering = ('created_at', 'updated_at')

    title = models.CharField(max_length=50, verbose_name='название навыка', unique=True)

    def __str__(self):
        return f'{self.title}'



class Education(TimeStampMixin):
    
    class Meta:
        verbose_name = 'образование'
        verbose_name_plural = 'образование'
        ordering = ('created_at', 'updated_at')

    level = models.CharField(max_length=30, choices=EUDCATION_LEVELS, verbose_name='уровень')
    education_institution = models.CharField(max_length=100, verbose_name='учебное заведение')
    faculty = models.CharField(max_length=100, verbose_name='факультет')
    specialization = models.CharField(max_length=100, verbose_name='cпециализация')
    year_of_ending = models.PositiveSmallIntegerField(verbose_name='год окончания')

    def __str__(self):
        return f'{self.education_institution} - {self.faculty}'


class ForeignLanguages(TimeStampMixin):

    class Meta:
        verbose_name = 'язык'
        verbose_name_plural = 'языки'
        ordering = ('created_at', 'updated_at')

    title = models.CharField(max_length=40, verbose_name='название иностранных языка', unique=True)

    def __str__(self):
        return f'{self.title}'


class JobExperience(TimeStampMixin):

    class Meta:
        verbose_name = 'опыт работы'
        verbose_name_plural = 'опыт работ'
        ordering = ('created_at', 'updated_at')

    start_date = models.DateField(verbose_name='начало работы')
    end_date = models.DateField(verbose_name='окончание работы')
    orgonization = models.CharField(max_length=100, verbose_name='организация')
    position = models.CharField(max_length=100, verbose_name='должность')
    description = models.CharField(max_length=500, verbose_name='описание место работы')

    def __str__(self):
        return f'{self.orgonization}'