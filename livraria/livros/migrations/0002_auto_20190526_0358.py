# Generated by Django 2.2.1 on 2019-05-26 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='quantidade_paginas',
        ),
        migrations.AddField(
            model_name='livro',
            name='descricao',
            field=models.CharField(blank=True, max_length=600),
        ),
        migrations.AddField(
            model_name='livro',
            name='quantidade_estoque',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='livro',
            name='quantitade_paginas',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livro',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
