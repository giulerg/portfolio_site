from django.db import models

# Create your models here.

class Project (models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    github_link = models.URLField(blank=True, null=True) 
    main_image = models.ImageField(upload_to='project_images/')
    created = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')