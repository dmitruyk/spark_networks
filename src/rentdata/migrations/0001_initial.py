# Generated by Django 2.1 on 2019-03-22 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('contact_form_type', models.CharField(max_length=80, verbose_name='contactFormType')),
                ('remove_creation', models.DateTimeField(blank=True, null=True)),
                ('remove_id', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='id')),
                ('remove_modification', models.DateTimeField(blank=True, null=True)),
                ('remove_publishDate', models.DateTimeField(blank=True, null=True)),
                ('xlink_href', models.CharField(default=None, max_length=280, verbose_name='xlink_href')),
                ('adLinkForJSONP_xlink_href', models.TextField(default=None, verbose_name='adLinkForJSONP_xlink_href')),
                ('adLinkForXMLData_xlink_href', models.TextField(default=None, verbose_name='adLinkForXMLData_xlink_href')),
            ],
            options={
                'db_table': 'apartment',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('companyWideCustomerId', models.CharField(default=None, max_length=80, verbose_name='companyWideCustomerId')),
                ('contactDetails_id', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='contactDetails_id')),
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
                ('contactDetails_faxNumberSubscriber', models.CharField(default=None, max_length=10, verbose_name='contactDetails_faxNumberSubscriber')),
                ('contactDetails_firstname', models.CharField(default=None, max_length=30, verbose_name='contactDetails_firstname')),
                ('contactDetails_homepageUrl', models.CharField(default=None, max_length=150, verbose_name='contactDetails_homepageUrl')),
                ('contactDetails_lastname', models.CharField(default=None, max_length=30, verbose_name='contactDetails_lastname')),
                ('contactDetails_phoneNumber', models.CharField(default=None, max_length=50, verbose_name='contactDetails_phoneNumber')),
                ('contactDetails_phoneNumberAreaCode', models.CharField(default=None, max_length=50, verbose_name='contactDetails_phoneNumberAreaCode')),
                ('contactDetails_phoneNumberCountryCode', models.CharField(default=None, max_length=10, verbose_name='contactDetails_phoneNumberCountryCode')),
                ('contactDetails_phoneNumberSubscriber', models.CharField(default=None, max_length=20, verbose_name='contactDetails_phoneNumberSubscriber')),
                ('contactDetails_salutation', models.CharField(default=None, max_length=10, verbose_name='contactDetails_salutation')),
                ('contactFormConfiguration_addressField', models.CharField(default=None, max_length=10, verbose_name='contactFormConfiguration_addressField')),
                ('contactFormConfiguration_applicationPackageCompletedField', models.CharField(default=None, max_length=10, verbose_name='contactFormConfiguration_applicationPackageCompletedField')),
                ('contactFormConfiguration_emailAddressField', models.CharField(default=None, max_length=10, verbose_name='contactFormConfiguration_emailAddressField')),
                ('contactFormConfiguration_employmentRelationshipField', models.CharField(default=None, max_length=10, verbose_name='contactFormConfiguration_employmentRelationshipField')),
                ('contactFormConfiguration_firstnameField', models.CharField(default=None, max_length=10, verbose_name='contactFormConfiguration_firstnameField')),
                ('contactFormConfiguration_freemiumSettings_duratio', models.PositiveIntegerField(default=0)),
                ('contactFormConfiguration_incomeField', models.CharField(default=None, max_length=10, verbose_name='contactFormConfiguration_incomeField')),
                ('contactFormConfiguration_lastnameField', models.CharField(default=None, max_length=10, verbose_name='contactFormConfiguration_lastnameField')),
                ('contactFormConfiguration_messageField', models.CharField(default=None, max_length=40, verbose_name='contactFormConfiguration_messageField')),
                ('contactFormConfiguration_moveInDateField', models.CharField(default=None, max_length=40, verbose_name='contactFormConfiguration_moveInDateField')),
                ('contactFormConfiguration_numberOfPersonsField', models.CharField(default=None, max_length=40, verbose_name='contactFormConfiguration_numberOfPersonsField')),
                ('contactFormConfiguration_petsInHouseholdField', models.CharField(default=None, max_length=40, verbose_name='contactFormConfiguration_petsInHouseholdField')),
                ('contactFormConfiguration_phoneNumberField', models.CharField(default=None, max_length=40, verbose_name='contactFormConfiguration_phoneNumberField')),
                ('contactFormConfiguration_premiumProfileRequired', models.CharField(default=None, max_length=40, verbose_name='contactFormConfiguration_premiumProfileRequired')),
                ('contactFormConfiguration_salutationField', models.CharField(default=None, max_length=40, verbose_name='contactFormConfiguration_salutationField')),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='ImprintLink',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('imprintLink_xlink_href', models.CharField(default=None, max_length=100, verbose_name='imprintLink_xlink_href')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='imprintLink_xlink_href', to='rentdata.Company')),
            ],
            options={
                'db_table': 'imprintLink',
            },
        ),
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('realEstate_id', models.PositiveIntegerField(blank=True, default=0, null=True, unique=True, verbose_name='id')),
                ('realEstate_xsi_type', models.CharField(default=None, max_length=50, verbose_name='realEstate_xsi_type')),
                ('realEstate_address_city', models.CharField(default=None, max_length=50, verbose_name='realEstate_address_city')),
                ('realEstate_address_geoHierarchy_city_fullGeoCodeId', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='realEstate_address_geoHierarchy_city_fullGeoCodeId')),
                ('realEstate_address_geoHierarchy_city_geoCodeId', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='realEstate_address_geoHierarchy_city_geoCodeId')),
                ('realEstate_address_geoHierarchy_city_name', models.CharField(default=None, max_length=150, verbose_name='realEstate_address_geoHierarchy_city_name')),
                ('realEstate_address_geoHierarchy_country_name', models.CharField(default=None, max_length=150, verbose_name='realEstate_address_geoHierarchy_country_name')),
                ('realEstate_address_geoHierarchy_quarter_fullGeoCodeId', models.CharField(default=None, max_length=150, verbose_name='realEstate_address_geoHierarchy_quarter_fullGeoCodeId')),
                ('realEstate_address_geoHierarchy_region_name', models.CharField(default=None, max_length=150, verbose_name='realEstate_address_geoHierarchy_region_name')),
                ('realEstate_address_postcode', models.CharField(default=None, max_length=150, verbose_name='realEstate_address_postcode')),
                ('x_link_href', models.CharField(default=None, max_length=280, verbose_name='x_link_href')),
                ('apartment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_rent', to='rentdata.Apartment')),
            ],
            options={
                'db_table': 'real_estate',
            },
        ),
        migrations.CreateModel(
            name='RealEstateAttachments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('modification', models.DateTimeField(blank=True, null=True)),
                ('creation', models.DateTimeField(blank=True, null=True)),
                ('publishDate', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(default=None, max_length=250, verbose_name='title')),
                ('real_estate_construction_year', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='real_estate_construction_year')),
                ('realEstate_externalId', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='realEstate_externalId')),
                ('realEstate_floor', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='realEstate_floor')),
                ('apartment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='real_estate_attachments', to='rentdata.RealEstate')),
            ],
            options={
                'db_table': 'realestate_attachments',
            },
        ),
        migrations.CreateModel(
            name='RealEstateTitlePictureUrls',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('apartment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Real_EstateTitlePictureUrls', to='rentdata.RealEstateAttachments')),
            ],
            options={
                'db_table': 'RealEstateTitlePictureUrls',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'status',
            },
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('apartment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='real_url', to='rentdata.RealEstateAttachments')),
            ],
            options={
                'db_table': 'url',
            },
        ),
        migrations.AddField(
            model_name='apartment',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_rent', to='rentdata.Company'),
        ),
    ]
