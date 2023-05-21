# Generated by Django 4.1.3 on 2023-05-20 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=25)),
                ('desc', models.TextField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_mis_Ajour', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_creation'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='Pas de nom', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('corps', models.TextField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_mis_Ajour', models.DateTimeField(auto_now=True)),
                ('contenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='poste.article')),
            ],
            options={
                'ordering': ['-date_creation'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poste.category'),
        ),
    ]