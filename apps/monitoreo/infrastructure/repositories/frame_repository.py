from apps.monitoreo.application.repositories_interfaces.frame_repository_interface import FrameRepositoryInterface
from apps.monitoreo.domain.models.frame_model import FrameModel
class FrameRepository(FrameRepositoryInterface):
    def __init__(self):
        super().__init__()

    def check_if_is_blinking(self, frame_model: FrameModel):
        return frame_model
