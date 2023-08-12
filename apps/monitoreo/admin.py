from django.contrib import admin

from apps.monitoreo.forms import FormVideoCall, ReportForm, ReportScreenshotForm, ReportTypeForm
from .models import ReportType, Report, ReportScreenshot, VideoCall

class ReportTypeAdmin(admin.ModelAdmin):
    form = ReportTypeForm
    list_display = ('id', 'description', 'url', 'zoom', 'target_iterations')

    def get_queryset(self, request):
        return self.model.custom_objects.get_queryset()

class ReportAdmin(admin.ModelAdmin):
    form = ReportForm
    list_display = ('name', 'code', 'description', 'created_at')

    def get_queryset(self, request):
        return self.model.custom_objects.get_queryset()

class ReportScreenshotAdmin(admin.ModelAdmin):
    form = ReportScreenshotForm
    list_display = ('name', 'path', 'report', 'report_type')

    def get_queryset(self, request):
        return self.model.custom_objects.get_queryset()
    
    
class VideoCallAdmin(admin.ModelAdmin):
    form = FormVideoCall
    list_display = ('name','path', 'blinks')


admin.site.register(ReportType, ReportTypeAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(ReportScreenshot, ReportScreenshotAdmin)
admin.site.register(VideoCall, VideoCallAdmin)