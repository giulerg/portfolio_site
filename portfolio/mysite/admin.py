from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'main_image')  
    search_fields = ('title', 'description')   
    list_filter = ('title','created')   

# Регистрация модели с настройками
admin.site.register(Project, ProjectAdmin)
