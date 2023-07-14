from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='images',blank=True, null=True)
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=20000)
    authors = models.ForeignKey(
         'auth.User',
         on_delete=models.CASCADE

    )



    def __str__(self):
        return self.title

class Contacts(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(auto_created=False)
    number = models.IntegerField()
    body = models.TextField(max_length=300)
    
    
    def __str__(self) -> str:
        return self.name