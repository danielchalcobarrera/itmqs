from rest_framework import serializers
from .models import Catedratico, Avance_materia
from .models import Materia
from .models import Tema
from .models import Contenido, Reporte_semanal

class CatedraticoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Catedratico
        fields="__all__"
        
class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields="__all__"
        
class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tema
        fields="__all__"
        
class ContenidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenido
        fields="__all__"       
        
        
class Reporte_semanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte_semanal
        fields="__all__"   
        
class Avance_materiaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Avance_materia
        fields="__all__"        


    # cedula_identidad = serializers.CharField()
class ReporteSemanalCatedraticoSerializer(serializers.Serializer):
    catedratico = CatedraticoSerializer(many=True)
    reporte_semanal = Reporte_semanalSerializer(many=True)
    