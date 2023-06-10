from django.db import models

# Create your models here.

class Recipe(models.Model):
    
    recipe_name = models.CharField(max_length=255)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='recipe')
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.recipe_name