from django.db import models


class Department(models.Model):
    title = models.CharField(verbose_name='Название', max_length=400)


class Workers(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Департамент')
    fio = models.CharField(verbose_name='ФИО', max_length=400)
    phone = models.CharField(verbose_name='Телефон', max_length=15)
    sellery = models.IntegerField()