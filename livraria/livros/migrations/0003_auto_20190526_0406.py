# Generated by Django 2.2.1 on 2019-05-26 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_auto_20190526_0358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='quantitade_paginas',
            new_name='quantidade_paginas',
        ),
    ]
