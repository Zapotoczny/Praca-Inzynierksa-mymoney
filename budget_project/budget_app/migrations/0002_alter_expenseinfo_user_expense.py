# Generated by Django 3.2.7 on 2021-09-21 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseinfo',
            name='user_expense',
            field=models.CharField(max_length=20),
        ),
    ]