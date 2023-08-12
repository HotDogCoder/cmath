from apps.monitoreo.application.repositories_interfaces.report_type_repository_interface import ReportTypeRepositoryInterface
from apps.monitoreo.domain.models.report_type_model import ReportTypeModel
from apps.monitoreo.infrastructure.serializers.report_type_serializer import ReportTypeSerializer
from apps.monitoreo.models import ReportType
class ReportTypeRepository(ReportTypeRepositoryInterface):
    def __init__(self):
        super().__init__()

    def get_report_type(self, report_type_model: ReportTypeModel):
        report_types = ReportType.custom_objects.all()
        
        serializer_class = ReportTypeSerializer(report_types, many=True)
        report_type_model.report_types = serializer_class.data
        return report_type_model
