# Generated by Django 3.0.2 on 2021-06-01 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0003_eventos_talleres'),
    ]

    operations = [
        migrations.AddField(
            model_name='talleres',
            name='autor',
            field=models.CharField(default=1, max_length=200, verbose_name='Autor Taller'),
            preserve_default=False,
        ),
    ]
