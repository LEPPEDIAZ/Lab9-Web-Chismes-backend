from django.db import models

#se implementa estos dos como metodos de prueba
class Note(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
class Body(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
#se implementa el Chisme
class Chisme(models.Model):
    titulo = models.CharField(max_length=255)
    chisme = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

