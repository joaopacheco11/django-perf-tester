# Generated by Django 3.2.2 on 2021-05-12 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('select_perf_tester', '0010_alter_testmodel1_ifield2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel1',
            name='index_field',
            field=models.IntegerField(default=0, verbose_name='Index Field'),
        ),
    ]
