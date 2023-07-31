from django.db import models

# Create your models here.
class Signature(models.Model):
    numberInput = models.CharField('Номер Входящий',null=True,blank=True,max_length=1000)
    user = models.CharField('Подпись пользователя',blank=True,null=True,max_length=2000)
    nomenklatura = models.CharField('Номенклатура',null=True,blank=True,max_length=1000)

class InputJournal(models.Model):
    choices_otdel = (
        ('01','01'),('02','02'),
        ('03','03'),('04','04'),
        ('05','05'),('06','06'),
        ('07','07'),('08','08'),
        ('09','09'),('10','10'),
        ('11','11'),('12','12'),
        ('13','13'),('14','14'),
        ('15','15'),('16','16'),
        ('17','17'),('18','18'),
        ('19','19'),('20','20'),
        ('21','21'),('22','22'),
        ('23','23'),('24','24'),
        ('25','25'),('26','26'),
        ('27','27'),('28','28'),
        ('29','29'),
    )
    #Это ключ к другой таблице. Signature - таблица к которой ты хочешь законектится
    signature = models.ForeignKey(Signature,on_delete=models.CASCADE,null=True, blank=True)
    #Поле для ввода чисел
    numberInput = models.CharField('Номер Входящий',null=True,blank=True,max_length=1000,choices=choices_otdel)
    dateReg = models.DateField('Дата регистрации',null=True,blank=True)
    correspondent = models.CharField('Кореспондент (откуда поступило)',null=True,blank=True,max_length=10000)
    content = models.CharField('Краткое содержание',null=True,blank=True,max_length=10000)
    #departament = models.CharField('Отдел',null=True,blank=True,max_length=1000)
    executor = models.CharField('Исполнитель',null=True,blank=True,max_length=10000)
    # поле для ввода дата формата 2022-12-08
    mark = models.CharField('Отметка о получении', null=True, blank=True, max_length=1000)
    nomenklatura = models.CharField('Номенклатура',null=True,blank=True,max_length=1000)