from django.contrib import admin
from .models import Summaries, Occupations, Citizenships, Skills, Education, ForeignLanguages, JobExperience

class AdminSummary(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'first_name', 
        'surname', 
        'phone_number', 
        'city',
    )

    search_fields = ('id', 'user', 'surname', 'salary', 'first_name',)
    list_filter = ('occupations', 'currency', 'foreign_language', 'isDistantWork', 'isMoving',)
    list_display_links = ('id', 'user',)

admin.site.register(Summaries, AdminSummary)


class AdminOccupations(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_field = ('id', 'title',)

admin.site.register(Occupations, AdminOccupations)
    

class AdminCitizenships(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_field = ('id', 'title',)

admin.site.register(Citizenships, AdminCitizenships)


class AdminSkills(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_field = ('id', 'title',)

admin.site.register(Skills, AdminSkills)


class AdminEducation(admin.ModelAdmin):
    list_display = ('id', 'level', 'education_institution', 'year_of_ending',)
    search_field = ('id', 'level', 'education_institution', 'faculty', 'specialization',)
    list_display_links = ('id', 'level',)

admin.site.register(Education, AdminEducation)


class AdminForeignLanguages(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_field = ('id', 'title',)

admin.site.register(ForeignLanguages)


class AdminJobExperience(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'end_date', 'orgonization', 'position',)
    search_field = ('id','start_date', 'end_date', 'orgonization', 'position',)
    list_filter = ('start_date', 'end_date',)

admin.site.register(JobExperience, AdminJobExperience)

# Register your models here.
