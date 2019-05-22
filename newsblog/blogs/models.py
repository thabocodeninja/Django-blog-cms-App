from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length =100)
    slug = models.SlugField()
    body = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    thumb =models.ImageField(default='default.png',blank=True)

    #add in thumbnail later
    #add in author later
    def __str__(self):
       return self.title

    def snipped(self):
        return self.body[:150]