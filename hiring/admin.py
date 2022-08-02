from django.contrib import admin
from .models import Tags, Hiring

class AdminHiring(admin.ModelAdmin):
    list_display = (
        'id',
        'company',
        'title',
        'salary',
        'occupation',
        'description',
        'first_phone_number',
        'second_phone_number',
    )
    list_display_links = ('id', 'company', 'title',)
    list_editable = ('salary',)
    list_filter = ('company','salary','responses',)
    search_field = ('id', 'company', 'title', 'salary')


admin.site.register(Hiring, AdminHiring)


class AdminTags(admin.ModelAdmin):
    list_display = ('id','title')
    search_fields = ('id','title')
admin.site.register(Tags, AdminTags)
# Register your models here.
