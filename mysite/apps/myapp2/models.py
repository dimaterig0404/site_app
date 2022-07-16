# from tabnanny import verbose
# from statistics import mode
from email.policy import default
from enum import Flag
from operator import mod
from django.db import models
import random
from django.utils.timezone import now

from .infos import *

grade_list = grade_list_()
grade_list_city = grade_list_city_()
grade_list_pol = grade_list_pol_()


# python manage.py makemigrations myapp
# python manage.py sqlmigrate myapp 0001 #инфо по базе 
# python manage.py migrate
# python manage.py shell
# from myapp.models import USER
# USER.objects.all()

class DATA_ALL_SEANSES(models.Model):
    ident_key = models.CharField('Специальный код сеанса',max_length=20,default=''.join(random.sample(list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'), len(list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')))[:15]))
    img = models.ImageField(verbose_name=u'Фото', upload_to='img/seans', null=True, blank=True)
    name = models.CharField('Имя сеанса',max_length=50)
    discription = models.TextField('Описание сеанса')
    categori = models.CharField('Возрастное ограничение (6,12,18)',max_length=5)
    summa = models.IntegerField('Цена билета', default=random.randint(200,1500))
    date = models.CharField('Дата мероприятия',max_length=50)#models.DateTimeField(default=now, blank=True)
    class_seans = models.IntegerField(choices=grade_list, default=3)
    isPush = models.BooleanField('По пушкинской можно оплатить',default=False)
    mesto = models.CharField('Место проведения мероприятия',max_length=50,default='')
    class Meta:
        verbose_name = 'Сеанс_афишы'
        verbose_name_plural = 'Сеансы_афиши'
    def __str__(self):
        return str(self.ident_key)+'|'+str(self.name)+'|'+str(self.categori)
class USER(models.Model):
    login = models.CharField('Никнейм пользователя', max_length=25)# Маленький текст
    password = models.CharField('Пароль пользователя', max_length=41)# Маленький текст
    age = models.SmallIntegerField('Возвраст пользователя',default=0)
    city = models.IntegerField(choices=grade_list_city, default=1)
    pol = models.IntegerField(choices=grade_list_pol, default=1)
    isGreen = models.BooleanField('Показатель если пользоветель по лицу то true',default=0)
    info_vac = models.CharField('ИНФО о вакцинации формат дата',max_length=50,blank=True)
    sopose = models.CharField('Qr, 18, med',max_length=5,blank=True)
    email = models.EmailField('Email пользователя',max_length=30)
    loock_like = models.IntegerField(choices=grade_list, default=3)
    likes = models.ManyToManyField(DATA_ALL_SEANSES)
    # my_friends = models.ManyToManyField("self",blank=True)
    list_frends = models.ManyToManyField("self",blank=True)
    list_req_frends =  models.ManyToManyField("self",blank=True)
    
    ico = models.ImageField(upload_to='img_user/',default='img/no_photo.png')
    class Meta:
        verbose_name = 'Пользователь_информация'
        verbose_name_plural = 'Пользователи_информация'
    def __str__(self):
        return f'{self.login}/{self.email}/{self.password}'
class II(models.Model):
    id_user = models.ForeignKey(USER,on_delete=models.CASCADE)
    info_photo = models.CharField('Инфо лица',max_length=3000,blank=True)
    now = models.ManyToManyField(DATA_ALL_SEANSES)
    code = models.CharField('Специальный код',max_length=12,blank=True)
    
    def __str__(self):
        return str(self.code)+"/"+str(self.id_user)
    
    def isCode_num(self):
        return True if self.code.isdigit() else False
    
    class Meta:
        verbose_name = 'Пользователь_лицо'
        verbose_name_plural = 'Пользователи_лица'

    
class SEANS(models.Model):
    id_user = models.ForeignKey(USER,on_delete=models.CASCADE)
    seanses = models.ManyToManyField(DATA_ALL_SEANSES)
    
    class Meta:
        verbose_name = 'Пользователь_сеанс'
        verbose_name_plural = 'Пользователи_сеансы'
    def __str__(self):
        return str(self.id_user)+'|'+str(self.seanses)


class Tegs(models.Model):
    name = models.CharField('Имя тега',max_length=50)
    events = models.ManyToManyField(DATA_ALL_SEANSES)
    
    class Meta:
        verbose_name = 'Тэг_для_поиска'
        verbose_name_plural = 'Тэги_для_поиска'
    def __str__(self):
        return str(self.name)