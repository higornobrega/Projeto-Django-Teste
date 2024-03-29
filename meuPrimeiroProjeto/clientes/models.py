from django.db import models

# Create your models here.
class Person (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    #Lembrar de instalar o Pillow (pip install Pillow)
    #upload_to caso queira salvar a imagem em uma pasta especial dentro de media
    #null = True  e blank = True faz o campo ser opcional
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True) 

    def __str__(self):
        return self.first_name + ' ' + self.last_name

