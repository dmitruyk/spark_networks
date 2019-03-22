# Generated by Django 2.1.7 on 2019-03-18 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentdata', '0003_auto_20190318_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('companyWideCustomerId', models.CharField(default=None, max_length=80, verbose_name='companyWideCustomerId')),
                ('contactDetails_id', models.PositiveIntegerField(blank=True, default=0, null=True, unique=True, verbose_name='contactDetails_id')),
                ('contactDetails_address_city', models.CharField(default=None, max_length=80, verbose_name='contactDetails_address_city')),
                ('contactDetails_address_houseNumber', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='contactDetails_id')),
                ('contactDetails_address_postcode', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='contactDetails_address_postcode')),
                ('contactDetails_address_street', models.CharField(default=None, max_length=180, verbose_name='contactDetails_address_street')),
                ('contactDetails_cellPhoneNumber', models.CharField(default=None, max_length=180, verbose_name='contactDetails_cellPhoneNumber')),
                ('contactDetails_cellPhoneNumberAreaCode', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='contactDetails_address_postcode')),
                ('contactDetails_cellPhoneNumberCountryCode', models.CharField(default=None, max_length=10, verbose_name='contactDetails_cellPhoneNumber')),
                ('contactDetails_cellPhoneNumberSubscribe', models.CharField(default=None, max_length=20, verbose_name='contactDetails_cellPhoneNumber')),
                ('contactDetails_company', models.CharField(default=None, max_length=180, verbose_name='contactDetails_cellPhoneNumber')),
                ('contactDetails_countryCode', models.CharField(default=None, max_length=10, verbose_name='contactDetails_cellPhoneNumber')),
                ('contactDetails_email', models.CharField(default=None, max_length=50, verbose_name='contactDetails_email')),
                ('contactDetails_faxNumber', models.CharField(default=None, max_length=50, verbose_name='contactDetails_faxNumber')),
                ('contactDetails_faxNumberAreaCode', models.CharField(default=None, max_length=10, verbose_name='contactDetails_faxNumberAreaCode')),
                ('contactDetails_faxNumberCountryCode', models.CharField(default=None, max_length=10, verbose_name='contactDetails_faxNumberCountryCode')),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.AddField(
            model_name='apartment',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_rent', to='rentdata.Company'),
        ),
    ]