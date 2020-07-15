# Generated by Django 3.0.6 on 2020-07-09 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Please enter title below 50 char', max_length=50, unique=True)),
                ('head0', models.CharField(max_length=500)),
                ('chead0', models.CharField(max_length=5000)),
                ('head1', models.CharField(max_length=500)),
                ('chead1', models.CharField(max_length=5000)),
                ('head2', models.CharField(max_length=500)),
                ('chead2', models.CharField(max_length=5000)),
                ('pub_date', models.DateField()),
                ('thumbnail', models.ImageField(blank=True, upload_to='images')),
                ('read', models.IntegerField(default=0)),
                ('author', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
