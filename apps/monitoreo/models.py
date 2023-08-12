from django.db import models

from apps.monitoreo.managers import ReportManager, ReportScreenshotManager, ReportTypeManager

class CustomDateTimeField(models.DateTimeField):
    def db_type(self, connection):
        if connection.vendor == 'microsoft':
            return 'datetime'
        return super().db_type(connection)

class VmwareMachine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    dato_1 = models.CharField(max_length=255)
    dato_2 = models.CharField(max_length=255)
    dato_3 = models.CharField(max_length=255)
    dato_4 = models.CharField(max_length=255)
    dato_5 = models.CharField(max_length=255)
    annotation = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    ram = models.IntegerField()
    processors = models.IntegerField()
    sockets = models.IntegerField()
    disk = models.IntegerField()
    os = models.CharField(max_length=255)
    lang = models.CharField(max_length=255)

class ReportType(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200, null=True)
    url = models.TextField(null=True)
    zoom = models.IntegerField(default=0)
    target_iterations = models.IntegerField(default=0)
    created_at = CustomDateTimeField(auto_now_add=True)
    
    custom_objects = ReportTypeManager()

    class Meta:
        db_table = 'report_types'

    def __str__(self):
        return self.description

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=True)
    code = models.CharField(max_length=20, null=True)
    description = models.TextField(null=True)
    created_at = CustomDateTimeField(auto_now_add=True)
    
    custom_objects = ReportManager()

    class Meta:
        db_table = 'reports'
    
    def __str__(self):
        return self.name

class ReportScreenshot(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    path = models.CharField(max_length=2000, null=True)
    created_at = CustomDateTimeField(auto_now_add=True)
    report = models.ForeignKey(Report, on_delete=models.CASCADE, db_column='report_id')
    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE, db_column='report_type_id')
    
    custom_objects = ReportScreenshotManager()

    class Meta:
        db_table = 'report_screenshots'
    
    def __str__(self):
        return f"{self.report.description} | {self.report_type.description}"
    
class VideoCall(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    path = models.CharField(max_length=2000, null=True)
    created_at = CustomDateTimeField(auto_now_add=True)
    blinks = models.IntegerField(default=0)
    
    custom_objects = ReportScreenshotManager()

    class Meta:
        db_table = 'video_calls'
    
    def __str__(self):
        return self.name
