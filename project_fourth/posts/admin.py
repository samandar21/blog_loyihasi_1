from django.contrib import admin
from .models import Articles,Comment
# Register your models here.

class CommentInLine(admin.TabularInline):
    model=Comment
    extra=0
    
class ArticleAdmin(admin.ModelAdmin):
    inlines=[CommentInLine]
    
admin.site.register(Comment)    
admin.site.register(Articles)

