# Generated by Django 2.0.2 on 2018-11-19 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
        ('user_operation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userleavingmessage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发起者'),
        ),
        migrations.AddField(
            model_name='userfav',
            name='acticle',
            field=models.ForeignKey(help_text='文章id', on_delete=django.db.models.deletion.CASCADE, to='blog.BlogActicle', verbose_name='文章'),
        ),
        migrations.AddField(
            model_name='userfav',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='usercomment',
            name='acticle',
            field=models.ForeignKey(help_text='文章id', on_delete=django.db.models.deletion.CASCADE, to='blog.BlogActicle', verbose_name='文章'),
        ),
        migrations.AddField(
            model_name='usercomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterUniqueTogether(
            name='userfav',
            unique_together={('user', 'acticle')},
        ),
        migrations.AlterUniqueTogether(
            name='usercomment',
            unique_together={('user', 'acticle')},
        ),
    ]
