from apps.monitoreo.application.services.frame_service import FrameService
from apps.monitoreo.domain.models.frame_model import FrameModel
class FrameController:
    def __init__(self):
        super().__init__()
        self.frame_service = FrameService()

    def check_if_is_blinking(self, frame_model: FrameModel):
        return self.frame_service.check_if_is_blinking(frame_model)
