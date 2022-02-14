# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)
    airport_name = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s - %s" % (self.name, self.airport_name)


class Airplane(models.Model):
    name = models.CharField(verbose_name=u"Название самолета", max_length=150)
    type = models.CharField(verbose_name=u"Тип самолета", max_length=50)

    def __unicode__(self):
        return "%s" % self.name


class Flight(models.Model):
    CHOICES = (
        (u"Вылетел", u"Вылетел"),
        (u"Приземлился", u"Приземлился"),
        (u"Идет посадка", u"Идет посадка"),
        (u"Задержка", u"Задержка"),
    )
    flight_number = models.CharField(verbose_name=u"Рейс",
                                     max_length=50)
    city_start = models.ForeignKey(City, verbose_name=u"Город вылета",
                                   on_delete=models.CASCADE,
                                   related_name='city_start')
    city_end = models.ForeignKey(City, verbose_name=u"Город прилета",
                                   on_delete=models.CASCADE,
                                 related_name='city_end')
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    start_time = models.TimeField(verbose_name=u"Время по расписанию")
    fact_time = models.TimeField(verbose_name=u"Время фактическое")
    status = models.CharField(max_length=300, choices=CHOICES)

    def __unicode__(self):
        return "%s" % self.flight_number

