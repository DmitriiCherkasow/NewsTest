# Generated by Django 4.1.5 on 2023-01-10 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news1', '0002_remove_post_article_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_rating',
            field=models.FloatField(default=0.0),
        ),
    ]
