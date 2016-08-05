from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class UserProfile(models.Model):
    """
    User Model.
    """
    GENDERS = (
        ('Female', 'Mujer'),
        ('Male', 'Hombre')
    )
    gender = models.CharField(max_length=100, choices=GENDERS, verbose_name="sexo")
    name = models.CharField(max_length=100, verbose_name="nombre")

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Product(models.Model):
    """
    Base product. This class will be inherited to use its behavior and fields.
    And it's used to set m2m relations with any product.
    """
    COLORS = (
        ('WHITE', 'Blanco'),
        ('BLACK', 'Negro'),
        ('GREEN', 'Verde'),
        ('RED', 'Rojo'),
        ('BLUE', 'Azul')
    )
    description =  models.CharField(max_length=255, default="New Product")
    precio =  models.PositiveIntegerField()
    color =  models.CharField(max_length=100, choices=COLORS, default='WHITE')
    peso = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.description


@python_2_unicode_compatible
class Order(models.Model):
    """
    Order model. Manage states, users and can add products.
    """
    STATES = (
        ('INTENDED', 'Preorden'),
        ('IN_PROGRESS', 'En Progreso'),
        ('CANCELLED', 'Cancelada'),
        ('SUCCESSFUL', 'Exitosa')
    )
    state = models.CharField(max_length=100, choices=STATES, default='INTENDED',verbose_name="estado")
    user = models.ForeignKey(UserProfile, verbose_name="usuario")
    date_created = models.DateTimeField(default=datetime.datetime.now, verbose_name="fecha de creacion")
    products = models.ManyToManyField(Product)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return "%s %s - %s" % (self.date_created.strftime('%Y-%m-%d'), self.state, self.user)


class Laptop(Product):
    """
    <Product> Laptop Model. 
    """
    procesador = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)


class Camara(Product):
    """
    <Product> Camara Model. 
    """
    TYPE = (
        ('DIGITAL', 'Digital'),
        ('REFLEX', 'Reflex')
    )
    tipo = models.CharField(max_length=100, choices=TYPE, default='DIGITAL')
    mpx = models.PositiveIntegerField(blank=True, null=True)


class Minicomponente(Product):
    """
    <Product> Minicomponente Model. 
    """
    potencia = models.CharField(max_length=10)
    reproduccion_usb =  models.BooleanField()
