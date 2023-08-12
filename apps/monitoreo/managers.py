from django.db import models

class ReportTypeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().using('monitoreo')

class ReportManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().using('monitoreo')

class ReportScreenshotManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().using('monitoreo')