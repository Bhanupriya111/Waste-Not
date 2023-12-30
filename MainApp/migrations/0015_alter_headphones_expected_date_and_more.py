# Generated by Django 4.1.1 on 2023-04-30 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0014_headphones_keyboards_laptops_mouse_phones_speakers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headphones',
            name='expected_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='keyboards',
            name='expected_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='laptops',
            name='expected_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='mouse',
            name='expected_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='phones',
            name='expected_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='speakers',
            name='expected_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='tvs',
            name='expected_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='watches',
            name='expected_date',
            field=models.DateTimeField(null=True),
        ),
    ]
