# Generated by Django 3.2.1 on 2021-05-06 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210505_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(blank=True, default='', null=True, to='app.Author'),
        ),
    ]
