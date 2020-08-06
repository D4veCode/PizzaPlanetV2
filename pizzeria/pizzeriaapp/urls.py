from django.urls import include, path
from rest_framework import routers
from . import views

#Aquí abajo se agregan las rutas del backend con su respectivo viewSet
router = routers.DefaultRouter()
router.register(r'pedidos', views.PedidoViewSet)
router.register(r'reporte1', views.Reporte1ViewSet)
router.register(r'reporte2', views.Reporte2ViewSet)
router.register(r'reporte3', views.Reporte3ViewSet)
router.register(r'reporte4', views.Reporte4ViewSet)
router.register(r'reporte5', views.Reporte5ViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]