# Generated by Django 3.2.13 on 2023-01-09 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office_dev', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputjournal',
            name='numberInput',
            field=models.CharField(blank=True, choices=[('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29')], max_length=1000, null=True, verbose_name='Номер Входящий'),
        ),
    ]
