# Generated by Django 3.2.2 on 2021-05-12 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Team name', max_length=50)),
                ('image', models.ImageField(help_text='Upload the team logo', upload_to='team_website')),
                ('url', models.URLField(help_text='Team website URL')),
            ],
        ),
    ]
