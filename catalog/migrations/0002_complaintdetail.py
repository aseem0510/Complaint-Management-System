# Generated by Django 3.1.7 on 2022-01-02 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeOfComplaint', models.CharField(max_length=50)),
                ('complaintDetail', models.TextField()),
                ('remark', models.CharField(default='Submitted', max_length=30)),
                ('complaintDate', models.DateTimeField(auto_now_add=True)),
                ('user_Key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compDetail', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
