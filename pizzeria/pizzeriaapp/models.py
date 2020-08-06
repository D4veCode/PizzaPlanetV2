from django.db import models

class Pedido(models.Model):
    date = models.DateField(auto_now_add=True)
    user = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    pizza = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    ingredientes = models.CharField(max_length = 200)

    def __str__(self):
        return str(self.id)+' '+self.user+' '+str(self.date)

class Cliente(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cedula = models.CharField(max_length=20)

    def __str__(self):
        return self.name+' '+self.lastname

class Base(models.Model):
    fk_pedido = models.IntegerField()
    tamano = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.tamano

class Ingrediente(models.Model):
    name = models.CharField(max_length=50)
    tamano = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name+' '+self.tamano

class Pizza(models.Model):
    fk_ingrediente = models.IntegerField()
    fk_base = models.IntegerField()

    def __str__(self):
        return str(self.fk_base)+' '+str(self.tamano)