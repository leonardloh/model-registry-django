# views.py

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Project, Model, Version, Metadata, Performance, Status
from .serializers import ProjectSerializer, ModelSerializer, VersionSerializer, MetadataSerializer, PerformanceSerializer, StatusSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(detail=True, methods=['get'])
    def all_models_details(self, request, pk=None):
        project = self.get_object()
        models = Model.objects.filter(project=project)
        
        result = []
        for model in models:
            model_data = ModelSerializer(model).data
            versions = Version.objects.filter(model=model)
            model_data['versions'] = []
            
            for version in versions:
                version_data = VersionSerializer(version).data
                version_data['metadata'] = MetadataSerializer(Metadata.objects.filter(version=version), many=True).data
                version_data['performance'] = PerformanceSerializer(Performance.objects.filter(version=version), many=True).data
                version_data['status'] = StatusSerializer(Status.objects.filter(version=version).first()).data
                model_data['versions'].append(version_data)
            
            result.append(model_data)
        
        return Response(result)

class ModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows models to be viewed or edited.
    """
    queryset = Model.objects.all()
    serializer_class = ModelSerializer

class VersionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows model versions to be viewed or edited.
    """
    queryset = Version.objects.all()
    serializer_class = VersionSerializer

class MetadataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows metadata to be viewed or edited.
    """
    queryset = Metadata.objects.all()
    serializer_class = MetadataSerializer

class PerformanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows performance metrics to be viewed or edited.
    """
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

class StatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows model status to be viewed or edited.
    """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer