import base64

from requests import request
from apps.monitoreo.ai.code.drowsiness_detector import DrowsinessDetector
from apps.monitoreo.application.services_interfaces.frame_service_interface import FrameServiceInterface
from apps.monitoreo.infrastructure.repositories.frame_repository import FrameRepository
from apps.monitoreo.domain.models.frame_model import FrameModel
import cv2
import os
from apps.monitoreo.models import VideoCall

from core.util.path.path_helper import PathHelper

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
from keras.models import load_model
import numpy as np
from pygame import mixer
import time


class FrameService(FrameServiceInterface):
    def __init__(self):
        super().__init__()
        self.frame_repository = FrameRepository()

    def check_if_is_blinking(self, frame_model: FrameModel):

        video_call = VideoCall.custom_objects.get(id=1)
        blinks = video_call.blinks
        frame_model.blinks = blinks

        print(blinks)

        drowsiness_detector = DrowsinessDetector()
        result = drowsiness_detector.detect_blink(frame_model)

        if result.get("action") == "RESET":

            video_call.blinks = 0
            video_call.save()

        # Return a JsonResponse with the result
        frame_model.tools = result.get("tools")
        frame_model.image = result.get("image", "")

        return self.frame_repository.check_if_is_blinking(frame_model)
