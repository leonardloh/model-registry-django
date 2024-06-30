# models.py
from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

class Model(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='models')
    model_name = models.CharField(max_length=200)
    model_description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

class Version(models.Model):
    model = models.ForeignKey('Model', on_delete=models.CASCADE, related_name='versions')
    version = models.IntegerField()  # Changed from CharField to IntegerField
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['model', 'version']  # Ensure version numbers are unique per model

    def __str__(self):
        return f"{self.model.model_name} - v{self.version}"

class Metadata(models.Model):
    version = models.ForeignKey(Version, on_delete=models.CASCADE, related_name='metadata')
    key = models.CharField(max_length=100)
    value = models.TextField()

class Performance(models.Model):
    version = models.ForeignKey(Version, on_delete=models.CASCADE, related_name='performance')
    key = models.CharField(max_length=100)
    value = models.TextField()

class Status(models.Model):
    version = models.ForeignKey(Version, on_delete=models.CASCADE, related_name='status')
    model_status = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now_add=True)