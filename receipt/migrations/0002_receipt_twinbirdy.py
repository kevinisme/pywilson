# Generated by Django 3.2.3 on 2021-05-27 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twinbird', '0001_initial'),
        ('receipt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='twinbirdy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='twinbird.twinbird'),
        ),
    ]
