# Generated by Django 3.1.7 on 2021-09-18 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompetitionResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('file_size', models.IntegerField(default=0)),
                ('file_name', models.CharField(default='', max_length=300)),
                ('file_show_name', models.CharField(default='', max_length=300)),
                ('type', models.CharField(choices=[('rank', '榜单'), ('problem_answer', '题解'), ('participate_manual', '参赛手册'), ('paper', '(集训队)论文'), ('data', '(XCPC)题目数据'), ('courseware', '课件'), ('others', '其他')], default='', max_length=300)),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('view_count', models.IntegerField(default=0)),
                ('download_count', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-upload_time'],
            },
        ),
    ]