# Generated by Django 4.1.1 on 2023-05-01 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0019_delete_vendorstocks'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorStocks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vendor_id', models.CharField(max_length=50)),
                ('pin', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('good_headphone_stocks', models.IntegerField(default=0)),
                ('best_headphone_stocks', models.IntegerField(default=0)),
                ('poor_headphone_stocks', models.IntegerField(default=0)),
                ('good_speaker_stocks', models.IntegerField(default=0)),
                ('best_speaker_stocks', models.IntegerField(default=0)),
                ('poor_speaker_stocks', models.IntegerField(default=0)),
                ('good_tv_stocks', models.IntegerField(default=0)),
                ('best_tv_stocks', models.IntegerField(default=0)),
                ('poor_tv_stocks', models.IntegerField(default=0)),
                ('good_laptop_stocks', models.IntegerField(default=0)),
                ('best_laptop_stocks', models.IntegerField(default=0)),
                ('poor_laptop_stocks', models.IntegerField(default=0)),
                ('good_keyboard_stocks', models.IntegerField(default=0)),
                ('best_keyboard_stocks', models.IntegerField(default=0)),
                ('poor_keyboard_stocks', models.IntegerField(default=0)),
                ('good_mouse_stocks', models.IntegerField(default=0)),
                ('best_mouse_stocks', models.IntegerField(default=0)),
                ('poor_mouse_stocks', models.IntegerField(default=0)),
                ('good_phone_stocks', models.IntegerField(default=0)),
                ('best_phone_stocks', models.IntegerField(default=0)),
                ('poor_phone_stocks', models.IntegerField(default=0)),
                ('good_watch_stocks', models.IntegerField(default=0)),
                ('best_watch_stocks', models.IntegerField(default=0)),
                ('poor_watch_stocks', models.IntegerField(default=0)),
            ],
        ),
    ]