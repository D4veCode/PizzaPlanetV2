from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PedidoSerializer
from .models import Pedido

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all().order_by('date')
    serializer_class = PedidoSerializer

class Reporte1ViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.filter(date='2020-08-06')
    serializer_class = PedidoSerializer

class Reporte5ViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all().order_by('user')
    serializer_class = PedidoSerializer