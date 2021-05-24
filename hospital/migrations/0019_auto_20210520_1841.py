# Generated by Django 3.0.5 on 2021-05-20 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital', '0018_auto_20200928_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/HospitalProfilePic/')),
                ('loction', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospital',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='hospital.Hospital'),
        ),
    ]
