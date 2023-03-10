# Generated by Django 4.1.5 on 2023-02-19 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_no', models.CharField(blank=True, max_length=200, null=True)),
                ('recorddate', models.DateField(blank=True, null=True)),
                ('patient_name', models.CharField(blank=True, max_length=200, null=True)),
                ('occupation', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('age', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Rather not to say', 'Rather not to say')], default='', max_length=100, null=True)),
                ('address', models.TextField(blank=True, default='', null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('email', models.EmailField(blank=True, default='', max_length=1000, null=True)),
                ('guardian_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('refferance', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('drug_allergy', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=200, null=True)),
                ('name_drug_allergy', models.CharField(blank=True, default='', max_length=2000, null=True)),
                ('rheumatic_fever', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=200, null=True)),
                ('valvular_diseases', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=200, null=True)),
                ('asthma_tb', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=200, null=True)),
                ('hypertension', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=200, null=True)),
                ('heart_desease', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=200, null=True)),
                ('heart_valve_pace_maker', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=200, null=True)),
                ('peptic_ulcer', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=200, null=True)),
                ('jaundice_liver_disease', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=200, null=True)),
                ('diabetes', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=200, null=True)),
                ('kidney_disease', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=200, null=True)),
                ('epilepsy', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=200, null=True)),
                ('bleeding_disorder', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=200, null=True)),
                ('hepa_b_c_hiv', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=200, null=True)),
                ('take_any_vaccine', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=200, null=True)),
                ('vaccine_type', models.CharField(blank=True, default='', max_length=400, null=True)),
                ('drug_history_name_if_any', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('last_dental_check_up_date', models.DateField(blank=True, null=True)),
                ('last_treatment_type', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('habits_addiction_name', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('experience_tooth_extraction_anaesthesia', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=200, null=True)),
                ('pregnancy', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='', max_length=200, null=True)),
                ('month_pregnant', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('lmp_date', models.DateField(blank=True, null=True)),
                ('other_information', models.TextField(blank=True, default='', null=True)),
                ('treatment_date', models.DateField(blank=True, null=True)),
                ('procedure', models.TextField(blank=True, default='', null=True)),
                ('next_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'patientinformation',
            },
        ),
    ]
