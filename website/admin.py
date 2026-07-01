from django.contrib import admin
from .models import Post,Contact
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','status','created_date')
    list_filter = ('status',)
    search_fields = ['title','content']

admin.site.register(Post,PostAdmin)

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name','subject','created_date')
    search_fields = ['name']

admin.site.register(Contact,ContactAdmin)