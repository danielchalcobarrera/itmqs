from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router  = DefaultRouter()
router.register(r"catedraticos", views.CatedraticoViewSet)
router.register(r"materias",views.MateriaViewSet)
router.register(r"temas",views.TemaViewSet)
router.register(r"contenidos",views.ContenidoViewSet)
router.register(r"reportes_semanales",views.Reporte_semanalViewSet)

urlpatterns = [
    #path('catedraticos/',views.catedraticos, name='catedraticos'),
    path('saludo/', views.index),
    path('', include(router.urls)),
    #genericAPIView
    path('reportessemanales/', views.ReporteSemanalCreateView.as_view()),
    #DRF Custom API
    path('catedra/cantidad/', views.catedraticos_count),
    path('reporte/avances/<str:ci>', views.reporte_avances_catedratico),
]