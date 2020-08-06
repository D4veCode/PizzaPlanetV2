from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PedidoSerializer
from .models import Pedido

class PedidoViewSet(viewsets.ModelViewSet):
    """Se devuelven todos los pedidos"""
    queryset = Pedido.objects.all().order_by('date')
    serializer_class = PedidoSerializer

class Reporte1ViewSet(viewsets.ModelViewSet):
    """Se devuelven todos los pedidos"""
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class Reporte2ViewSet(viewsets.ModelViewSet):
    """Se ordena la lista de acuerdo a la fecha del pedido"""
    queryset = Pedido.objects.all().order_by('date')
    serializer_class = PedidoSerializer

class Reporte3ViewSet(viewsets.ModelViewSet):
    """Se ordena la lista de acuerdo al tamaño de la Pizza"""
    queryset = Pedido.objects.all().order_by('size')
    serializer_class = PedidoSerializer

class Reporte4ViewSet(viewsets.ModelViewSet):
    """Se ordena la lista de acuerdo a los ingredientes"""
    queryset = Pedido.objects.all().order_by('ingredientes')
    serializer_class = PedidoSerializer

class Reporte5ViewSet(viewsets.ModelViewSet):
    """Se ordena la lista de acuerdo a el nombre del usuario"""
    queryset = Pedido.objects.all().order_by('user')
    serializer_class = PedidoSerializer