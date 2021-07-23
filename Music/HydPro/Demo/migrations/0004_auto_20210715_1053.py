# Generated by Django 2.2.17 on 2021-07-15 10:53

from django.db import migrations
import pgcrypto.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Demo', '0003_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=pgcrypto.fields.EmailPGPSymmetricKeyField(max_length=254),
        ),
        migrations.AlterField(
            model_name='person',
            name='salary',
            field=pgcrypto.fields.IntegerPGPSymmetricKeyField(),
        ),
    ]
