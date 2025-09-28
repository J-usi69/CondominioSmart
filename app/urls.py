# app/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from app.views.auth import EmailOrUsernameTokenObtainPairView
from app.views.residencia import ResidenciaViewSet
from app.views.apartamento import ApartamentoViewSet
from app.views.residente import ResidenteAltaViewSet
<<<<<<< HEAD
=======
from app.views.residencia_asignar import ResidenciaAsignacionViewSet
from app.views.residente_usuario import ResidenteUsuarioViewSet
from app.views.propietario_usuario import PropietarioUsuarioViewSet
from app.views.propiedad_asignar import PropiedadAsignacionViewSet
from app.views.propietario_usuario import PropietarioListView, PropietarioDetailUpdateView
from app.views.apartamento import ApartamentoListView
from app.views.residente_usuario import ResidenteListView
from app.views.servicio import ServicioViewSet
from app.views.cargo import CargoViewSet
from app.views.pago import PagoViewSet
from app.views.vehiculo import VehiculoViewSet
from app.views.visita import VisitaViewSet
from app.views.auth_me import MeView
from app.views.usuario import UsuarioViewSet
from app.views.reserva import ReservaViewSet
from app.views.area_comun import AreaComunViewSet
from app.views.detalle_reserva import DetalleReservaViewSet
from app.views.pago import PagoViewSet
from app.views.acceso import (
    PuntoAccesoViewSet, CamaraViewSet,
    ReconocimientoViewSet, IntentoAccesoViewSet,
    EntradaSalidaViewSet
)
from app.views.reconocimiento_ia import ReconocerIAView

>>>>>>> riv/develop

urlpatterns = [

    path("auth/login/", EmailOrUsernameTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("residencias/", ResidenciaViewSet.as_view({'get': 'list', 'post': 'create'}), name="residencia-list"),
    path("apartamentos/", ApartamentoViewSet.as_view({'get': 'list', 'post': 'create'}), name="apartamento-list"),
    path("residentes/", ResidenteAltaViewSet.as_view({'post': 'create'}), name="residente-create"),
<<<<<<< HEAD
]
=======
    path("residencias/asignar/", ResidenciaAsignacionViewSet.as_view({'post': 'create'}), name="residencia-asignar"),
    path("usuarios-residentes/", ResidenteUsuarioViewSet.as_view({'post': 'create'}), name="usuario-residente-create"),
    path("usuarios-propietarios/", PropietarioUsuarioViewSet.as_view({'post': 'create'}), name="usuario-propietario-create"),
    path("propiedades/asignar/", PropiedadAsignacionViewSet.as_view({'post': 'create'}), name="propiedad-asignar"),
    path("propietarios/", PropietarioListView.as_view(), name="propietario-list"),
    path("propietarios/<int:pk>/", PropietarioDetailUpdateView.as_view(), name="propietario-detail-update"),
    path("apartamentos/list/", ApartamentoListView.as_view(), name="apartamento-list-view"),
    path("residentes/list/", ResidenteListView.as_view(), name="residente-list-view"),
    path("servicios/", ServicioViewSet.as_view({'get': 'list', 'post': 'create'}), name="servicio-list"),
    path("cargos/", CargoViewSet.as_view({'get': 'list', 'post': 'create'}), name="cargo-list"),
    path("pagos/", PagoViewSet.as_view({'get': 'list', 'post': 'create'}), name="pago-list"),
    path("vehiculos/", VehiculoViewSet.as_view({'get': 'list', 'post': 'create'}), name="vehiculo-list"),   
    path("visitas/", VisitaViewSet.as_view({'get': 'list', 'post': 'create'}), name="visita-list"),
    path("visitas/registrar/", VisitaViewSet.as_view({'post': 'registrar'}), name="visita-registrar"),
    path("auth/me/", MeView.as_view(), name="auth-me"),
    path("usuarios/", UsuarioViewSet.as_view({'get': 'list', 'post': 'create'}), name="usuario-list"),
    path("reservas/", ReservaViewSet.as_view({'get': 'list', 'post': 'create'}), name="reserva-list"),
    path("areas-comunes/", AreaComunViewSet.as_view({'get': 'list', 'post': 'create'}), name="areacomun-list"),
    path("detalles-reserva/", DetalleReservaViewSet.as_view({'get': 'list', 'post': 'create'}), name="detalle-reserva-list"),
    path("usuarios/<int:pk>/", UsuarioViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="usuarios-detail"),
    path("visitas/<int:pk>/", VisitaViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="visitas-detail"),
    path("visitas/<int:pk>/cerrar/", VisitaViewSet.as_view({"post": "cerrar"}), name="visitas-cerrar"),
    path("vehiculos/<int:pk>/", VehiculoViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="vehiculos-detail"),
    path("areas-comunes/<int:pk>/", AreaComunViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="areacomun-detail"),
    path("reservas/<int:pk>/", ReservaViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="reservas-detail"),
    path("detalles-reserva/<int:pk>/", DetalleReservaViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="detalles-reserva-detail"),
    path("cargos/<int:pk>/", CargoViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="cargos-detail"),
    path("pagos/<int:pk>/aprobar/", PagoViewSet.as_view({"post": "aprobar"}), name="pagos-aprobar"),
    path("pagos/", PagoViewSet.as_view({'get': 'list', 'post': 'create'}), name="pago-list"),
    path("pagos/<int:pk>/", PagoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name="pago-detail"),
    path("pagos/<int:pk>/aprobar/", PagoViewSet.as_view({"post": "aprobar"}), name="pago-aprobar"),
    path("pagos/<int:pk>/rechazar/", PagoViewSet.as_view({"post": "rechazar"}), name="pago-rechazar"),
    #url de la camara
    path("puntos-acceso/", PuntoAccesoViewSet.as_view({"get": "list", "post": "create"}), name="puntosacceso-list"),
    path("puntos-acceso/<int:pk>/", PuntoAccesoViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="puntosacceso-detail"),
    path("camaras/", CamaraViewSet.as_view({"get": "list", "post": "create"}), name="camara-list"),
    path("camaras/<int:pk>/", CamaraViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="camara-detail"),
    path("reconocimientos/", ReconocimientoViewSet.as_view({"get": "list", "post": "create"}), name="reconocimiento-list"),
    path("reconocimientos/<int:pk>/", ReconocimientoViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="reconocimiento-detail"),
    path("reconocimientos/procesar/", ReconocimientoViewSet.as_view({"post": "procesar"}), name="reconocimiento-procesar"),
    path("intentos/", IntentoAccesoViewSet.as_view({"get": "list", "post": "create"}), name="intento-list"),
    path("intentos/<int:pk>/", IntentoAccesoViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="intento-detail"),
    path("entradas-salidas/", EntradaSalidaViewSet.as_view({"get": "list", "post": "create"}), name="entradasalida-list"),
    path("entradas-salidas/<int:pk>/", EntradaSalidaViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="entradasalida-detail"),
    path("reconocer-ia/", ReconocerIAView.as_view(), name="reconocer-ia"),
]
>>>>>>> riv/develop
