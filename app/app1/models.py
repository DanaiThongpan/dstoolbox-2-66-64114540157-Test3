from django.db import models

# Create your models here.
class DB(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.id}'