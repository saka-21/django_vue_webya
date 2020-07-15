# Generated by Django 3.0.3 on 2020-07-15 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200716_0023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='カテゴリー名')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '商品カテゴリー',
                'verbose_name_plural': '商品カテゴリー',
            },
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': '商品', 'verbose_name_plural': '商品'},
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Category'),
        ),
    ]