# Generated by Django 3.2.9 on 2021-11-23 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0004_receita_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/'),
        ),
    ]
