import json
import re
from rest_framework.views import APIView
from apps.monitoreo.domain.models import speak_model
from apps.monitoreo.domain.models.cmath_model import CmathModel
from apps.monitoreo.domain.models.frame_model import FrameModel
from apps.monitoreo.domain.models.report_type_model import ReportTypeModel
from apps.monitoreo.domain.models.rsa_model import RsaModel
from apps.monitoreo.domain.models.screenshot import Screenshot
from apps.monitoreo.domain.models.speak_model import SpeakModel
from apps.monitoreo.domain.models.speech_model import SpeechModel
from apps.monitoreo.presentation.controllers.cmath_controller import CmathController
from apps.monitoreo.presentation.controllers.congruence_controller import CongruenceController
from apps.monitoreo.presentation.controllers.frame_controller import FrameController
from apps.monitoreo.presentation.controllers.report_type_controller import ReportTypeController
from apps.monitoreo.presentation.controllers.rsa_controller import RsaController

from apps.monitoreo.presentation.controllers.screenshot_controller import ScreenshotController
from django.http import HttpResponse
from apps.monitoreo.presentation.controllers.speech_controller import SpeechController

class StartMonitoreo(APIView):
    def post(self, request, format=None):
        driver = 'Chrome'
        image_name_prefix = 'screenshot_'

        request_data = self.request.data

        screenshot = Screenshot(
            url="https://demo-acp.calimaco.com/",
            image_name_prefix=image_name_prefix,
            driver=driver,
            id=request_data['id'],
            to=request_data['to']
        )

        SC = ScreenshotController()
        SS = SC.take_screenshot_of_servers_status_1(screenshot=screenshot)

        print('------------- termino -----------------')
        print(SS.image_list)

        json_data = json.dumps({
            'image_paths': SS.paths,
            'request_data': request_data
        })
        
        return HttpResponse(json_data, content_type='application/json')

class ReportTypeView(APIView):
    def post(self, request, format=None):
        request_data = self.request.data

        report_type_model = ReportTypeModel()

        RC = ReportTypeController()
        RC = RC.get_report_type(report_type_model=report_type_model)

        json_data = json.dumps(vars(RC))
        return HttpResponse(json_data, content_type='application/json')

    def get(self, request, format=None):
        # text = request.GET.get('text', '')
        # if not text:
        #     return HttpResponseBadRequest("Missing 'text' parameter")

        report_type_model = ReportTypeModel()

        RC = ReportTypeController()
        RC = RC.get_report_type(report_type_model=report_type_model)

        json_data = json.dumps(vars(RC))
        return HttpResponse(json_data, content_type='application/json')

class ImageProcessorView(APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)  # Parse the JSON body
        frame_model = FrameModel()

        frame_model.frame= data.get('frame', None)
        frame_model.frame= re.sub('^data:image/.+;base64,', '', frame_model.frame)
        frame_model.bytes_data=data.get('bytes_data')
        frame_model.base_data=data.get('base_data')

        FC = FrameController()
        FS = FC.check_if_is_blinking(frame_model=frame_model)

        print('------------- termino -----------------')

        json_data = json.dumps(vars(FS))
        
        return HttpResponse(json_data, content_type='application/json')
    
class CmathView(APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)  # Parse the JSON body
        cmath_model = CmathModel()

        # cmath_model.cmath= data.get('cmath', None)
        # cmath_model.cmath= re.sub('^data:image/.+;base64,', '', cmath_model.cmath)
        # cmath_model.bytes_data=data.get('bytes_data')
        # cmath_model.base_data=data.get('base_data')

        CC = CmathController()
        CC.set_test_list(cmath_model=cmath_model)
        CC.test_cmath(cmath_model=cmath_model)

        print('------------- termino -----------------')

        json_data = json.dumps(cmath_model.to_dict())
        
        return HttpResponse(json_data, content_type='application/json')
    
class SpeechView(APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)  # Parse the JSON body
        speech_model = SpeechModel()

        speech_model.input = data.get('input', '')

        SC = SpeechController()
        SC = SC.run_speech(speech_model=speech_model)

        print('------------- termino -----------------')

        json_data = json.dumps(vars(SC))
        
        return HttpResponse(json_data, content_type='application/json')
    
class CongruenceView(APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)  # Parse the JSON body
        congruence_model = CmathModel()

        # cmath_model.cmath= data.get('cmath', None)
        # cmath_model.cmath= re.sub('^data:image/.+;base64,', '', cmath_model.cmath)
        # cmath_model.bytes_data=data.get('bytes_data')
        # cmath_model.base_data=data.get('base_data')

        CC = CongruenceController()
        CC.set_test_list(congruence_model=congruence_model)
        CC.test_congruence(congruence_model=congruence_model)

        print('------------- termino -----------------')

        json_data = json.dumps(congruence_model.to_dict())
        
        return HttpResponse(json_data, content_type='application/json')
    
class RsaView(APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)  # Parse the JSON body
        rsa_model = RsaModel()

        # cmath_model.cmath= data.get('cmath', None)
        # cmath_model.cmath= re.sub('^data:image/.+;base64,', '', cmath_model.cmath)
        # cmath_model.bytes_data=data.get('bytes_data')
        # cmath_model.base_data=data.get('base_data')

        RC = RsaController()
        RC.set_test_list(rsa_model=rsa_model)
        RC.test_rsa(rsa_model=rsa_model)

        print('------------- termino -----------------')

        json_data = json.dumps(rsa_model.to_dict())
        
        return HttpResponse(json_data, content_type='application/json')