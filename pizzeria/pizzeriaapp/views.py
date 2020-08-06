from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PedidoSerializer
from .models import Pedido

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all().order_by('date')
    serializer_class = PedidoSerializer