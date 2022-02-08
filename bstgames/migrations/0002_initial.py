# Generated by Django 3.2.6 on 2022-02-08 04:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bstgames', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamemarket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='gamegameplatform',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bstgames.game'),
        ),
        migrations.AddField(
            model_name='gamegameplatform',
            name='gameplatform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bstgames.gameplatform'),
        ),
        migrations.AddField(
            model_name='gamegamegenre',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bstgames.game'),
        ),
        migrations.AddField(
            model_name='gamegamegenre',
            name='gamegenre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bstgames.gamegenre'),
        ),
        migrations.AddField(
            model_name='game',
            name='developer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bstgames.gamedeveloper', verbose_name='Developer'),
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ManyToManyField(blank=True, through='bstgames.GameGameGenre', to='bstgames.GameGenre', verbose_name='Genre'),
        ),
        migrations.AddField(
            model_name='game',
            name='platform',
            field=models.ManyToManyField(blank=True, through='bstgames.GameGamePlatform', to='bstgames.GamePlatform', verbose_name='Platform'),
        ),
        migrations.AddField(
            model_name='game',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bstgames.gamepublisher', verbose_name='Publisher'),
        ),
        migrations.AddConstraint(
            model_name='gamegameplatform',
            constraint=models.UniqueConstraint(fields=('game', 'gameplatform'), name='unique_game_gameplatform'),
        ),
        migrations.AddConstraint(
            model_name='gamegamegenre',
            constraint=models.UniqueConstraint(fields=('game', 'gamegenre'), name='unique_game_gamegenre'),
        ),
    ]