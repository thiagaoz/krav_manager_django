# Generated by Django 3.2.6 on 2021-09-10 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210909_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='data_inscricao',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Inscrição'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Nascimento'),
        ),
    ]
