# Generated by Django 5.1.4 on 2025-01-14 04:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=255)),
                ('name_kg', models.CharField(max_length=255)),
                ('name_en', models.CharField(max_length=255)),
                ('icon', models.URLField(blank=True, null=True)),
                ('priority', models.IntegerField()),
                ('iiko_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModelStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=255)),
                ('name_en', models.CharField(max_length=255)),
                ('name_kg', models.CharField(max_length=255)),
                ('logo', models.URLField(blank=True, null=True)),
                ('gif', models.URLField(blank=True, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('address_link', models.URLField(blank=True, null=True)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('desc_ru', models.TextField()),
                ('desc_en', models.TextField()),
                ('desc_kg', models.TextField()),
                ('iiko_id', models.CharField(blank=True, max_length=255, null=True)),
                ('login', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='News',
            new_name='ModelNews',
        ),
        migrations.RenameModel(
            old_name='Story',
            new_name='ModelStory',
        ),
        migrations.RemoveField(
            model_name='address',
            name='city',
        ),
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='item',
        ),
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.RemoveField(
            model_name='category',
            name='stores',
        ),
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.RemoveField(
            model_name='item',
            name='store',
        ),
        migrations.RemoveField(
            model_name='order',
            name='store',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='workinghours',
            name='store',
        ),
        migrations.RemoveField(
            model_name='user',
            name='major',
        ),
        migrations.RenameModel(
            old_name='City',
            new_name='ModelCity',
        ),
        migrations.CreateModel(
            name='ModelAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('type', models.CharField(choices=[('apt', 'Apartment'), ('house', 'House')], max_length=5)),
                ('floor', models.CharField(blank=True, max_length=10, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modelcity')),
            ],
        ),
        migrations.CreateModel(
            name='ModelItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=255)),
                ('name_en', models.CharField(max_length=255)),
                ('name_kg', models.CharField(max_length=255)),
                ('photo', models.URLField(blank=True, null=True)),
                ('gif', models.URLField(blank=True, null=True)),
                ('desc_ru', models.TextField()),
                ('desc_en', models.TextField()),
                ('desc_kg', models.TextField()),
                ('cost', models.FloatField()),
                ('is_sale', models.BooleanField(default=False)),
                ('sale_cost', models.FloatField(blank=True, null=True)),
                ('is_available', models.BooleanField(default=True)),
                ('is_hit', models.BooleanField(default=False)),
                ('is_new', models.BooleanField(default=False)),
                ('iiko_id', models.CharField(blank=True, max_length=255, null=True)),
                ('priority', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('photo_from_api', models.URLField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modelcategory')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modelstore')),
            ],
        ),
        migrations.CreateModel(
            name='ModelCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.FloatField()),
                ('sold_cost_one', models.FloatField()),
                ('comment', models.TextField(blank=True, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modelitem')),
            ],
        ),
        migrations.CreateModel(
            name='ModelAdditional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=255)),
                ('name_en', models.CharField(max_length=255)),
                ('name_kg', models.CharField(max_length=255)),
                ('cost', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modelitem')),
            ],
        ),
        migrations.AddField(
            model_name='modelcategory',
            name='stores',
            field=models.ManyToManyField(to='core.modelstore'),
        ),
        migrations.RenameModel(
            old_name='Major',
            new_name='ModelMajor',
        ),
        migrations.CreateModel(
            name='ModelUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('birthday', models.DateField()),
                ('avatar', models.URLField(blank=True, null=True)),
                ('scores', models.FloatField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('date_registered', models.DateTimeField(auto_now_add=True)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modelmajor')),
            ],
        ),
        migrations.CreateModel(
            name='ModelOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('new', 'New'), ('confirmed', 'Confirmed'), ('cooking', 'Cooking'), ('ready', 'Ready'), ('finished', 'Finished'), ('cancelled', 'Cancelled')], max_length=10)),
                ('type', models.CharField(choices=[('togo', 'To Go'), ('delivery', 'Delivery')], max_length=10)),
                ('total_cost', models.FloatField()),
                ('paid_with_score', models.FloatField()),
                ('total_to_pay', models.FloatField()),
                ('is_paid', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('transaction_id', models.CharField(blank=True, max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('file_from_api', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modeladdress')),
                ('items', models.ManyToManyField(to='core.modelcartitem')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modelstore')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modeluser')),
            ],
        ),
        migrations.AddField(
            model_name='modeladdress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modeluser'),
        ),
        migrations.CreateModel(
            name='ModelWorkingHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modelstore')),
            ],
        ),
        migrations.DeleteModel(
            name='Additional',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Store',
        ),
        migrations.DeleteModel(
            name='WorkingHours',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]