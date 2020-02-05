from django.db import models

# Create your models here.
class boy (models.Model):
    images = models.ImageField(upload_to='images/',
    default='images/def.jpg',
    blank=True,
    null=True)
    nick_name = models.CharField(max_length = 20)
    character = models.TextField(max_length = 50)
    price = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.nick_name