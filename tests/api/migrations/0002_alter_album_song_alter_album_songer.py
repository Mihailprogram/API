# Generated by Django 4.2.5 on 2023-09-05 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='song',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.songs'),
        ),
        migrations.AlterField(
            model_name='album',
            name='songer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.songer'),
            preserve_default=False,
        ),
    ]
