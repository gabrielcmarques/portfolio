# Generated by Django 4.0.1 on 2022-05-28 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0004_projeto_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfil',
            options={},
        ),
        migrations.AlterModelOptions(
            name='projeto',
            options={},
        ),
        migrations.AlterField(
            model_name='projeto',
            name='tags',
            field=models.ManyToManyField(blank=True, to='projetos.Tag'),
        ),
    ]
