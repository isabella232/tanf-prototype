# Generated by Django 2.2.4 on 2019-08-30 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_auto_20190830_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adult',
            name='racehispanic',
            field=models.CharField(max_length=1, verbose_name='race/ethnicity: hispanic or latino (item 34a)'),
        ),
        migrations.AlterField(
            model_name='adult',
            name='racenativeamerican',
            field=models.CharField(max_length=1, verbose_name='race/ethnicity: american indian or alaska native (item 34b)'),
        ),
        migrations.AlterField(
            model_name='child',
            name='racehispanic',
            field=models.CharField(max_length=1, verbose_name='race/ethnicity: hispanic or latino (item 70a)'),
        ),
        migrations.AlterField(
            model_name='child',
            name='racenativeamerican',
            field=models.CharField(max_length=1, verbose_name='race/ethnicity: american indian or alaska native (item 70b)'),
        ),
        migrations.AlterField(
            model_name='closedcase',
            name='receivesfoodstamps',
            field=models.CharField(max_length=1, verbose_name='receives food stamps (item 12)'),
        ),
        migrations.AlterField(
            model_name='closedcase',
            name='receivesmedicalassistance',
            field=models.CharField(max_length=1, verbose_name='receives medical assistance (item 11)'),
        ),
        migrations.AlterField(
            model_name='closedcase',
            name='receivessubsidizedchildcare',
            field=models.CharField(max_length=1, verbose_name='receives subsidized child care (item 13)'),
        ),
        migrations.AlterField(
            model_name='closedcase',
            name='receivessubsidizedhousing',
            field=models.CharField(max_length=1, verbose_name='receives subsidized housing (item 10)'),
        ),
        migrations.AlterField(
            model_name='closedperson',
            name='nonssabenefits',
            field=models.CharField(max_length=1, verbose_name='receives disability benefits: receives benefits based on federal disability status under non-ssa programs (item 19b)'),
        ),
        migrations.AlterField(
            model_name='closedperson',
            name='oasdibenefits',
            field=models.CharField(max_length=1, verbose_name='receives disability benefits: received federal disability insurance benefits under the oasdi program (item 19a)'),
        ),
        migrations.AlterField(
            model_name='closedperson',
            name='parentminorchild',
            field=models.CharField(max_length=1, verbose_name='parent with minor child in the family (item 22)'),
        ),
        migrations.AlterField(
            model_name='closedperson',
            name='raceasian',
            field=models.CharField(max_length=1, verbose_name='race/ethnicity: asian (item 17c)'),
        ),
        migrations.AlterField(
            model_name='closedperson',
            name='raceblack',
            field=models.CharField(max_length=1, verbose_name='race/ethnicity: black or african american (item 17d)'),
        ),
        migrations.AlterField(
            model_name='closedperson',
            name='racehispanic',
            field=models.CharField(max_length=1, verbose_name='race/ethnicity: hispanic or latino (item 17a)'),
        ),
        migrations.AlterField(
            model_name='closedperson',
            name='racenativeamerican',
            field=models.CharField(max_length=1, verbose_name='race/ethnicity: american indian or alaska native (item 17b)'),
        ),
        migrations.AlterField(
            model_name='closedperson',
            name='racepacific',
            field=models.CharField(max_length=1, verbose_name='race/ethnicity: native hawaiian or other pacific islander (item 17e)'),
        ),
        migrations.AlterField(
            model_name='closedperson',
            name='racewhite',
            field=models.CharField(max_length=1, verbose_name='race/ethnicity: white (item 17f)'),
        ),
        migrations.AlterField(
            model_name='closedperson',
            name='titlexivapdtbenefits',
            field=models.CharField(max_length=1, verbose_name='receives disability benefits: received aid to the permanently and totally disabled under title xiv-apdt (item 19c)'),
        ),
        migrations.AlterField(
            model_name='closedperson',
            name='titlexviaabdbenefits',
            field=models.CharField(max_length=1, verbose_name='receives disability benefits: received aid to the aged, blind, and disabled under title xvi-aabd (item 19d)'),
        ),
        migrations.AlterField(
            model_name='closedperson',
            name='titlexvissibenefits',
            field=models.CharField(max_length=1, verbose_name='receives disability benefits: received ssi under title xvi-ssi (item 19e)'),
        ),
        migrations.AlterField(
            model_name='family',
            name='receivesfoodstamps',
            field=models.CharField(max_length=1, verbose_name='receives food stamps (item 15)'),
        ),
        migrations.AlterField(
            model_name='family',
            name='receivesmedicalassistance',
            field=models.CharField(max_length=1, verbose_name='receives medical assistance (item 14)'),
        ),
        migrations.AlterField(
            model_name='family',
            name='receivessubsidizedchildcare',
            field=models.CharField(max_length=1, verbose_name='receives food stamps (item 17)'),
        ),
        migrations.AlterField(
            model_name='family',
            name='receivessubsidizedhousing',
            field=models.CharField(max_length=1, verbose_name='receives subsidized housing (item 13)'),
        ),
    ]