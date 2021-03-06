# Generated by Django 2.2.1 on 2019-05-26 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0003_auto_20190526_0406'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialEscolar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.CharField(blank=True, max_length=600)),
                ('quantidade_estoque', models.IntegerField(blank=True, default=0)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('promocao', models.BooleanField(default=False)),
                ('categoria', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='livro',
            name='promocao',
            field=models.BooleanField(default=False),
        ),
    ]
