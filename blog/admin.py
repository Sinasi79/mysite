from django.contrib import admin
from .models import Post,Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','status','created_date')
    list_filter = ('status',)
    search_fields = ['title','content']
    summernote_fields = ('more_info',)

admin.site.register(Category)
admin.site.register(Post,PostAdmin)
