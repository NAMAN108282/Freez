# Generated by Django 3.1rc1 on 2020-08-13 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapi', '0012_auto_20200813_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='Food_Code',
            field=models.CharField(default='NULL', max_length=20, primary_key=True, serialize=False),
        ),
    ]
