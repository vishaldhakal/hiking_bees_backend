# Generated by Django 4.1.4 on 2023-02-02 18:02

from django.db import migrations, models
import django.db.models.deletion
import django_summernote.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_created=True)),
                ('activity_title', models.CharField(max_length=500)),
                ('slug', models.SlugField(max_length=100)),
                ('price', models.FloatField()),
                ('heroImg', models.ImageField(upload_to='')),
                ('ratings', models.FloatField()),
                ('coverImg', models.ImageField(upload_to='')),
                ('location', models.CharField(max_length=500)),
                ('duration', models.CharField(max_length=500)),
                ('trip_grade', models.CharField(max_length=500)),
                ('max_group_size', models.CharField(max_length=500)),
                ('best_time', models.CharField(max_length=500)),
                ('priceSale', models.FloatField(blank=True)),
                ('popular', models.BooleanField()),
                ('best_selling', models.BooleanField()),
                ('tour_description', django_summernote.fields.SummernoteTextField()),
                ('tour_highlights', django_summernote.fields.SummernoteTextField()),
                ('tour_includes', django_summernote.fields.SummernoteTextField()),
                ('tour_excludes', django_summernote.fields.SummernoteTextField()),
                ('availableStart', models.DateTimeField()),
                ('availableEnd', models.DateTimeField()),
            ],
            options={
                'ordering': ['createdAt'],
            },
        ),
        migrations.CreateModel(
            name='ActivityCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('slug', models.SlugField(blank=True)),
                ('image_alt_description', models.CharField(default='Alt Description', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('destination_detail', django_summernote.fields.SummernoteTextField(blank=True)),
                ('thumnail_image', models.ImageField(blank=True, upload_to='')),
                ('thumnail_image_alt_description', models.CharField(default='Alt Description', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ItineraryActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('trek_distance', models.CharField(max_length=100)),
                ('trek_duration', models.CharField(max_length=100)),
                ('highest_altitude', models.CharField(max_length=100)),
                ('meals', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itinerary', to='activity.activity')),
            ],
            options={
                'ordering': ['day'],
            },
        ),
        migrations.CreateModel(
            name='ActivityImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('image_alt_description', models.CharField(default='Image Description', max_length=428)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='activity.activity')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='activity.activitycategory'),
        ),
        migrations.AddField(
            model_name='activity',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='activity.destination'),
        ),
    ]
