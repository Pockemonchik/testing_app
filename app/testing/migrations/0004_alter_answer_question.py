# Generated by Django 4.2.5 on 2023-09-07 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0003_answer_delete_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='testing.question', verbose_name='Связанный вопрос'),
        ),
    ]
