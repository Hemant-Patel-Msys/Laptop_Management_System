from django.db import models


class Laptop(models.Model):
    name = models.CharField(max_length=100, verbose_name='Machine Name')
    email = models.EmailField(max_length=277, verbose_name='Email')
    comment = models.TextField(max_length=500, verbose_name='Text Area')
    id = models.IntegerField(primary_key=True,verbose_name='Machine_Id')


#def __str__(self):
    #return str(self.id)
