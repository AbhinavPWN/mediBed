# Generated by Django 4.2.4 on 2024-02-14 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('wrong_password_attempt', models.PositiveIntegerField(default=0)),
                ('last_logged_in_time', models.DateTimeField(blank=True, null=True)),
                ('is_super_admin', models.BooleanField(default=False)),
                ('is_central_admin', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=255)),
                ('created_by_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by_admin', to='services.admin')),
                ('deleted_by_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_deleted_by_admin', to='services.admin')),
            ],
            options={
                'db_table': 'hospital',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('status_desc', models.CharField(max_length=45)),
                ('icon', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'status',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('address', models.CharField(max_length=255)),
                ('other_details', models.TextField()),
                ('created_by_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by_admin', to='services.admin')),
                ('deleted_by_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_deleted_by_admin', to='services.admin')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.hospital')),
                ('updated_by_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by_admin', to='services.admin')),
            ],
            options={
                'db_table': 'patient',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('created_by_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by_admin', to='services.admin')),
                ('deleted_by_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_deleted_by_admin', to='services.admin')),
                ('updated_by_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by_admin', to='services.admin')),
            ],
            options={
                'db_table': 'location',
            },
        ),
        migrations.CreateModel(
            name='ICU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
                ('no_of_ward', models.PositiveIntegerField(default=0)),
                ('is_vacant', models.BooleanField(default=True)),
                ('created_by_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by_admin', to='services.admin')),
                ('deleted_by_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_deleted_by_admin', to='services.admin')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.hospital')),
                ('updated_by_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by_admin', to='services.admin')),
            ],
            options={
                'db_table': 'icu',
            },
        ),
        migrations.AddField(
            model_name='hospital',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.location'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='updated_by_admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by_admin', to='services.admin'),
        ),
        migrations.CreateModel(
            name='Ambulance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
                ('vehicle_number', models.CharField(max_length=50, unique=True)),
                ('ambulance_number', models.CharField(max_length=50)),
                ('created_by_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by_admin', to='services.admin')),
                ('deleted_by_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_deleted_by_admin', to='services.admin')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.hospital')),
                ('updated_by_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by_admin', to='services.admin')),
            ],
            options={
                'db_table': 'ambulance',
            },
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated_date', models.DateTimeField(auto_now=True)),
                ('message', models.TextField()),
                ('message_from', models.CharField(max_length=255)),
                ('created_by_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_created_by_admin', to='services.admin')),
                ('deleted_by_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_deleted_by_admin', to='services.admin')),
                ('updated_by_admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by_admin', to='services.admin')),
            ],
            options={
                'db_table': 'alert',
            },
        ),
    ]
