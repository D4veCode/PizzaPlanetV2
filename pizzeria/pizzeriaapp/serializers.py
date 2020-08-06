from rest_framework import serializers

from .models import Pedido

"""Esta clase se encarga de transformar el objeto a un objeto de tipo JSON"""
class PedidoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedido
        fields = ('id','date', 'user','price','pizza','size','ingredientes','cant')
