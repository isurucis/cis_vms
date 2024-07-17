# Generated by Django 4.0.6 on 2024-07-17 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='contact_person',
        ),
        migrations.AddField(
            model_name='contactperson',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contactperson',
            name='mobilenumber',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='contactperson',
            name='telnumber',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='ContactNumber',
        ),
        migrations.DeleteModel(
            name='Email',
        ),
    ]