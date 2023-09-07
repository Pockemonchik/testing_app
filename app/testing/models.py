from django.db import models
from django.contrib.postgres.fields import ArrayField



class Test(models.Model):
    """Класс для обьекта теста"""
    theme = models.CharField(max_length=50, null=True,
                             blank=True, verbose_name="Тема теста")
    description = models.TextField(
        null=True, blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"
        ordering = ["-id"]

    def __str__(self):
        try:
            if self.theme:
                return self.theme
            else:
                return str(self.id)
        except:
            return str(self.id)


class Question(models.Model):
    """Класс для впоросов к тесту"""
    test = models.ForeignKey(
        Test, related_name="questions", on_delete=models.CASCADE, verbose_name="Связанный тест")
    description = models.TextField(
        null=True, blank=True, verbose_name="Описание вопроса")

    class Meta:
        verbose_name = "Вопрос к тесту"
        verbose_name_plural = "Вопросы к тесту"
        ordering = ["-id"]

    def __str__(self):
        try:
            if self.description:
                return self.description
            else:
                return str(self.id)
        except:
            return str(self.id)


class Answers(models.Model):
    """Класс для ответов на вопрос из теста"""
    question = models.ForeignKey(Question, related_name="anwers",
                                 on_delete=models.CASCADE, verbose_name="Связанный вопрос")
    description = models.TextField(
        null=True, blank=True, verbose_name="Описание ответа")
    correct = models.BooleanField(default=False,verbose_name="Правильность")

    class Meta:
        verbose_name = "Ответ на вопрос"
        verbose_name_plural = "Ответы на вопрос"
        ordering = ["-id"]

    def __str__(self):
        try:
            if self.description:
                return self.description
            else:
                return str(self.id)
        except:
            return str(self.id)
