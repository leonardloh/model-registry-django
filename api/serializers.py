# serializers.py
from rest_framework import serializers
from .models import Project, Model, Version, Metadata, Performance, Status

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'

class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = '__all__'

    def validate(self, data):
        """
        Check that the version is unique for the model.
        """
        model = data.get('model')
        version = data.get('version')
        if Version.objects.filter(model=model, version=version).exists():
            raise serializers.ValidationError("This version already exists for this model.")
        return data

class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = '__all__'

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'