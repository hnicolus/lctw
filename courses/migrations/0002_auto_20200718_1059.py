# Generated by Django 2.2.2 on 2020-07-18 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instructor',
            old_name='name',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='skill',
            name='image',
            field=models.ImageField(null=True, upload_to='images/skills/'),
        ),
    ]
