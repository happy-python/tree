# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area',
            old_name='parent',
            new_name='parent_area',
        ),
    ]
