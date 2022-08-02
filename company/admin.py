from django.contrib import admin
from .models import Companies
from django.utils.safestring import mark_safe


class AdminCompanies(admin.ModelAdmin):
    list_display = ('id', 'get_img', 'title', 'information', 'owner')
    search_fields = ('id', 'title')  
    list_display_links = ('id', 'get_img', 'title',)
    fields = (
        'logo',
        'title',
        'information' ,
        'owner',
        'get_img',
        'created_at',
        'updated_at', 
    )

    readonly_fields = ('get_img', 'created_at', 'updated_at',)

    def get_img(self, obj):
        return mark_safe(f'<img src="{obj.logo.url}" style="width: 5rem;">')
    
    get_img.short_description = 'Логотип'
    
admin.site.register(Companies, AdminCompanies)

# Register your models here.