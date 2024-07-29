from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .models import Catedratico, Avance_materia
from .models import Materia, Tema, Contenido, Reporte_semanal
from .serializers import CatedraticoSerializer, Reporte_semanalSerializer, ReporteSemanalCatedraticoSerializer
from .serializers import MateriaSerializer, TemaSerializer, ContenidoSerializer
from rest_framework import generics
from rest_framework.decorators  import api_view  


def index(request):
    return HttpResponse("Hola  Reportes Semanales")

def catedraticos(request):
    return render(request, "catedraticos.html")

class CatedraticoViewSet(viewsets.ModelViewSet):
    queryset = Catedratico.objects.all()
    serializer_class = CatedraticoSerializer
    
class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
    
class TemaViewSet(viewsets.ModelViewSet):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer
    
class ContenidoViewSet(viewsets.ModelViewSet):
    queryset = Contenido.objects.all()
    serializer_class = ContenidoSerializer

class Reporte_semanalViewSet(viewsets.ModelViewSet):
    queryset = Reporte_semanal.objects.all()
    serializer_class = Reporte_semanalSerializer

# GenericApiView

class ReporteSemanalCreateView(generics.CreateAPIView,generics.ListAPIView):
    queryset=Reporte_semanal.objects.all()
    serializer_class = Reporte_semanalSerializer
    
    
 #DRF Custom API
 
@api_view(["GET"])
def catedraticos_count(request):
    """
    Cantidad de catedraticos activos
    """
    try:
        cantidad = Catedratico.objects.count()
        return JsonResponse(
            {
                "cantidad" : cantidad
            },
            status=200,
        )
    except Exception as e:
        return JsonResponse({
            "message": str(e)
            },
            status=400 
        )
#DRF Custom API
@api_view(["GET"])       
def reporte_avances_catedratico(request,ci):
        """
            Lista de  un catedratico y sus reportes de avance por semanas
        """ 
        print (ci)
        try:
            catedratico = Catedratico.objects.filter(cedula_identidad__contains=ci)
            idCatedratico = catedratico[0].id 
            reporte_semanal  =Reporte_semanal.objects.filter(catedratico_id=idCatedratico)
            
            #ci = Catedratico.objects.count()  filter(catedratico_id=1)
            print("id_catedratico:")
            print (idCatedratico)
            print("reporte_semanal:")
            print  (reporte_semanal)
            
            return JsonResponse(
                ReporteSemanalCatedraticoSerializer({
                    "catedratico": catedratico,
                    "reporte_semanal":reporte_semanal
                }).data,
                safe=False,
                status=200,
            )
        except Exception as e:
            return JsonResponse({"message":str(e)}, status=400)    