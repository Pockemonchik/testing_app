from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.timezone import localdate
from datetime import datetime, date



class Test(models.Model):
    """Класс для обьекта теста"""
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Имя")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"
        ordering = ["-id"]
    
    def __str__(self):
        try:
            if self.name:
                return self.name
            else:
                return str(self.id)
        except:
            return str(self.id)
        



