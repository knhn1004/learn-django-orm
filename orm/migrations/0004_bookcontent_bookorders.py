# Generated by Django 3.1.4 on 2020-12-19 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0003_auto_20201219_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookOrders',
            fields=[
            ],
            options={
                'ordering': ['created'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('orm.bookcontent',),
        ),
    ]
