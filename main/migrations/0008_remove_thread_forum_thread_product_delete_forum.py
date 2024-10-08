# Generated by Django 5.1.1 on 2024-10-08 19:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_forum_thread_reply_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='forum',
        ),
        migrations.AddField(
            model_name='thread',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='threads', to='main.product'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Forum',
        ),
    ]
