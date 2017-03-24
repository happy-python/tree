# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', models.ForeignKey(related_name='children', verbose_name=b'\xe4\xb8\x8a\xe7\xba\xa7\xe5\x8c\xba\xe5\x9f\x9f', blank=True, to='area.Area', null=True)),
            ],
            options={
                'db_table': 'area',
                'verbose_name': '\u7701/\u5e02/\u5730\u533a(\u53bf)',
                'verbose_name_plural': '\u7701/\u5e02/\u5730\u533a(\u53bf)',
            },
        ),
    ]
