from apps.monitoreo.application.services_interfaces.report_type_service_interface import ReportTypeServiceInterface
from apps.monitoreo.infrastructure.repositories.report_type_repository import ReportTypeRepository
from apps.monitoreo.domain.models.report_type_model import ReportTypeModel
class ReportTypeService(ReportTypeServiceInterface):
    def __init__(self):
        super().__init__()
        self.report_type_repository = ReportTypeRepository()

    def get_report_type(self, report_type_model: ReportTypeModel):
        return self.report_type_repository.get_report_type(report_type_model)
