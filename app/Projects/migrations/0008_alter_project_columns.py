# Generated by Django 4.1.7 on 2023-03-23 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0007_remove_projectcolumn_project_project_columns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='columns',
            field=models.ManyToManyField(null=True, related_name='projectcolumn_project', to='Projects.projectcolumn', verbose_name='Columns'),
        ),
    ]
