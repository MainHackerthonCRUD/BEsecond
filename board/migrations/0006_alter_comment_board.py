# Generated by Django 5.0.7 on 2024-07-25 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0005_board_blogcnt_board_maindoctorcnt_board_visitcnt"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="board",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="board.board",
            ),
        ),
    ]
