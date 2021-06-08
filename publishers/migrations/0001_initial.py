# Generated by Django 3.2.3 on 2021-06-08 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publishers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='出版社名')),
                ('phone_number', models.CharField(max_length=11, verbose_name='出版社电话')),
                ('email', models.EmailField(max_length=254, verbose_name='出版社邮箱')),
                ('contacts', models.CharField(max_length=20, verbose_name='联系人')),
                ('address', models.CharField(max_length=20, verbose_name='出版社地址')),
            ],
            options={
                'verbose_name': '出版社信息',
                'verbose_name_plural': '出版社信息',
            },
        ),
    ]
