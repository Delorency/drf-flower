# Generated by Django 4.1.7 on 2023-03-28 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskcard',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_taskcard_creators', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='taskcard',
            name='worker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_taskcard_workers', to=settings.AUTH_USER_MODEL, verbose_name='Worker'),
        ),
        migrations.AddField(
            model_name='projectcolumn',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_projectcolumn_creators', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
    ]
