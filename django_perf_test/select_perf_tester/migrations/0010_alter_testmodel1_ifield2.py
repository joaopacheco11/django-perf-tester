# Generated by Django 3.2.2 on 2021-05-12 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('select_perf_tester', '0009_alter_testmodel1_index_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel1',
            name='ifield2',
            field=models.IntegerField(verbose_name='Integer field 2'),
        ),
    ]