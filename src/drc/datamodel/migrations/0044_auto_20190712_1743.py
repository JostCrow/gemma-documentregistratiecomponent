# Generated by Django 2.2.2 on 2019-07-12 15:43

from django.db import migrations, models
import django.db.models.deletion
import vng_api_common.fields


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0043_merge_20190708_1204'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='objectinformatieobject',
            options={'verbose_name': 'Oobject-informatieobject', 'verbose_name_plural': 'object-informatieobjecten'},
        ),
        migrations.AlterField(
            model_name='enkelvoudiginformatieobject',
            name='formaat',
            field=models.CharField(blank=True, help_text='Het "Media Type" (voorheen "MIME type") voor de wijze waaropde inhoud van het INFORMATIEOBJECT is vastgelegd in een computerbestand. Voorbeeld: `application/msword`. Zie: https://www.iana.org/assignments/media-types/media-types.xhtml', max_length=255),
        ),
        migrations.AlterField(
            model_name='enkelvoudiginformatieobject',
            name='indicatie_gebruiksrecht',
            field=models.NullBooleanField(default=None, help_text='Indicatie of er beperkingen gelden aangaande het gebruik van het informatieobject anders dan raadpleging. Dit veld mag `null` zijn om aan te geven dat de indicatie nog niet bekend is. Als de indicatie gezet is, dan kan je de gebruiksrechten die van toepassing zijn raadplegen via de GEBRUIKSRECHTen resource.', verbose_name='indicatie gebruiksrecht'),
        ),
        migrations.AlterField(
            model_name='enkelvoudiginformatieobject',
            name='informatieobjecttype',
            field=models.URLField(help_text='URL-referentie naar het INFORMATIEOBJECTTYPE (in de Catalogi API).'),
        ),
        migrations.AlterField(
            model_name='enkelvoudiginformatieobject',
            name='integriteit_algoritme',
            field=models.CharField(blank=True, choices=[('crc_16', 'CRC-16'), ('crc_32', 'CRC-32'), ('crc_64', 'CRC-64'), ('fletcher_4', 'Fletcher-4'), ('fletcher_8', 'Fletcher-8'), ('fletcher_16', 'Fletcher-16'), ('fletcher_32', 'Fletcher-32'), ('hmac', 'HMAC'), ('md5', 'MD5'), ('sha_1', 'SHA-1'), ('sha_256', 'SHA-256'), ('sha_512', 'SHA-512'), ('sha_3', 'SHA-3')], help_text='Aanduiding van algoritme, gebruikt om de checksum te maken.', max_length=20, verbose_name='integriteit algoritme'),
        ),
        migrations.AlterField(
            model_name='enkelvoudiginformatieobject',
            name='status',
            field=models.CharField(blank=True, choices=[('in_bewerking', 'In bewerking'), ('ter_vaststelling', 'Ter vaststelling'), ('definitief', 'Definitief'), ('gearchiveerd', 'Gearchiveerd')], help_text="Aanduiding van de stand van zaken van een INFORMATIEOBJECT. De waarden 'in bewerking' en 'ter vaststelling' komen niet voor als het attribuut `ontvangstdatum` van een waarde is voorzien. Wijziging van de Status in 'gearchiveerd' impliceert dat het informatieobject een duurzaam, niet-wijzigbaar Formaat dient te hebben.", max_length=20, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='enkelvoudiginformatieobject',
            name='taal',
            field=models.CharField(help_text='Een ISO 639-2/B taalcode waarin de inhoud van het INFORMATIEOBJECT is vastgelegd. Voorbeeld: `nld`. Zie: https://www.iso.org/standard/4767.html', max_length=3),
        ),
        migrations.AlterField(
            model_name='enkelvoudiginformatieobject',
            name='vertrouwelijkheidaanduiding',
            field=vng_api_common.fields.VertrouwelijkheidsAanduidingField(blank=True, choices=[('openbaar', 'Openbaar'), ('beperkt_openbaar', 'Beperkt openbaar'), ('intern', 'Intern'), ('zaakvertrouwelijk', 'Zaakvertrouwelijk'), ('vertrouwelijk', 'Vertrouwelijk'), ('confidentieel', 'Confidentieel'), ('geheim', 'Geheim'), ('zeer_geheim', 'Zeer geheim')], help_text='Aanduiding van de mate waarin het INFORMATIEOBJECT voor de openbaarheid bestemd is.', max_length=20),
        ),
        migrations.AlterField(
            model_name='gebruiksrechten',
            name='informatieobject',
            field=models.ForeignKey(help_text='URL-referentie naar het INFORMATIEOBJECT.', on_delete=django.db.models.deletion.CASCADE, to='datamodel.EnkelvoudigInformatieObjectCanonical'),
        ),
        migrations.AlterField(
            model_name='objectinformatieobject',
            name='informatieobject',
            field=models.ForeignKey(help_text='URL-referentie naar het INFORMATIEOBJECT.', on_delete=django.db.models.deletion.CASCADE, to='datamodel.EnkelvoudigInformatieObjectCanonical'),
        ),
        migrations.AlterField(
            model_name='objectinformatieobject',
            name='object',
            field=models.URLField(help_text='URL-referentie naar het gerelateerde OBJECT (in deze of een andere API).'),
        ),
        migrations.AlterField(
            model_name='objectinformatieobject',
            name='object_type',
            field=models.CharField(choices=[('besluit', 'Besluit'), ('zaak', 'Zaak')], help_text='Het type van het gerelateerde OBJECT.', max_length=100, verbose_name='objecttype'),
        ),
    ]
