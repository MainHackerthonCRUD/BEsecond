# Generated by Django 5.0.7 on 2024-07-18 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_remove_customuser_university'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.CharField(default='', max_length=10, null=True),
        ),
    ]
