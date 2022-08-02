from django.contrib import admin
from .models import Orders

class AdminOrders(admin.ModelAdmin):
    list_display = (
        'id',
        'owner',
        'title', 
        'description',  
        'first_phone_number',
        'second_phone_number',
        'status',
        'maker',
        )
    search_field = ('id','title','owner','email','maker')
    list_display_links = ('id','title')
    list_filter = ('first_phone_number','second_phone_number')
    list_editable = ('owner','maker')

admin.site.register(Orders,AdminOrders)
