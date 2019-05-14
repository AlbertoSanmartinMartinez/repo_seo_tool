
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.
class Engine(models.Model):
    """
    """

    name = models.CharField(verbose_name='Nombre', max_length=100)
    url= models.URLField(verbose_name="URL")

    class Meta:
        verbose_name = "Motor de Búsqueda"
        verbose_name_plural = "Motores de Búsqueda"
        db_table = 'engine'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Search(models.Model):
    """
    """

    keywords = models.CharField(verbose_name="Palabras Clave", max_length=100)
    FRECUENCY = (('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'))
    frecuency = models.CharField(verbose_name="Frecuencia", max_length=7, choices=FRECUENCY, default='Monthly')
    engine = models.ForeignKey(Engine, verbose_name='Motor de Búsqueda', null=True, on_delete=models.SET_NULL, related_name='search_engine')

    class Meta:
        verbose_name = "Busqueda"
        verbose_name_plural = "Busquedas"
        db_table = 'search'

    def __str__(self):
        return str(self.keywords) + ' | ' + str(self.frecuency) + ' | ' + str(self.engine.name)

    def __unicode__(self):
        return str(self.keywords) + ' | ' + str(self.frecuency) + ' | ' + str(self.engine.name)


class Result(models.Model):
    """
    """

    date = models.DateField(verbose_name="Fecha", auto_now_add=True)
    url= models.URLField(verbose_name="URL")
    position = models.PositiveIntegerField(verbose_name="Posicion")
    search = models.ForeignKey(Search, verbose_name='Búsqueda', null=True, on_delete=models.SET_NULL, related_name='result_search')

    class Meta:
        verbose_name = "Resultado"
        verbose_name_plural = "Resultados"
        db_table = 'result'

    def __str__(self):
        return str(self.date) + ' | ' + str(self.url) + ' | ' + str(self.position) + ' | ' + str(self.search.id)

    def __unicode__(self):
        return str(self.date) + ' | ' + str(self.url) + ' | ' + str(self.position) + ' | ' + str(self.search.id)




#
