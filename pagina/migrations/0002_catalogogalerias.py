# Generated by Django 3.0.2 on 2021-06-01 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogoGalerias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_principal', models.ImageField(blank=True, null=True, upload_to='')),
                ('galeria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagina.Galerias')),
            ],
            options={
                'verbose_name': 'Catologo de Galeria',
                'verbose_name_plural': 'Catalogo de Galerias',
                'db_table': 'catalogo_galerias',
                'ordering': ['id'],
            },
        ),
    ]
