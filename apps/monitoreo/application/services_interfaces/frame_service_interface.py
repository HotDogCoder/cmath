from abc import ABC, abstractmethod
from apps.monitoreo.domain.models.frame_model import FrameModel
class FrameServiceInterface(ABC):
    def __init__(self):
        super().__init__()


    @abstractmethod
    def check_if_is_blinking(self, frame_model: FrameModel):
        return frame_model
