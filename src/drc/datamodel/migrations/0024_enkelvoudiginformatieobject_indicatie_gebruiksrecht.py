# Generated by Django 2.0.9 on 2018-12-17 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0023_enkelvoudiginformatieobject_ontvangstdatum'),
    ]

    operations = [
        migrations.AddField(
            model_name='enkelvoudiginformatieobject',
            name='indicatie_gebruiksrecht',
            field=models.NullBooleanField(default=None, help_text='Indicatie of er beperkingen gelden aangaande het gebruik van het informatieobject anders dan raadpleging.', verbose_name='indicatie gebruiksrecht'),
        ),
    ]