from django.db import models

class Pedido(models.Model):
    date = models.DateField(auto_now_add=True)
    user = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    pizza = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    ingredientes = models.CharField(max_length = 200)

    def __str__(self):
        return self.user + str(self.id)
