import base64
import numpy as np
import cv2
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from keras.models import load_model
from apps.monitoreo.domain.models.frame_model import FrameModel
from core.settings import APP_URL

from core.util.path.path_helper import PathHelper

class DrowsinessDetector:
    def detect_blink(self,frame_model: FrameModel):
        path_helper = PathHelper()
        # Load your models outside of the view function so it's only loaded once
        path = f"{path_helper.get_project_root_path()}/apps/monitoreo/ai/models"
        storage_path = f"{path_helper.get_project_root_path()}/media/monitoreo/"
        model = load_model(f"{path}/cnnCat8.h5")
        path = f"{path_helper.get_project_root_path()}/apps/monitoreo/ai/files"
        face = cv2.CascadeClassifier(f"{path}/haarcascade_frontalface_alt.xml")
        leye = cv2.CascadeClassifier(f"{path}/haarcascade_lefteye_2splits.xml")
        reye = cv2.CascadeClassifier(f"{path}/haarcascade_righteye_2splits.xml")
        
        data = {
            "success": False,
            "image": None,
            "tools": [],
            "action": "NONE"
        }

        tools = []
        canvas_tool = {
            "type": "rectangle",
            "x": 0,
            "y": 0,
            "w": 0,
            "h": 0,
            "color": "",
            "text": ""
        }
        # Convert base64 image to a numpy array
        nparr = np.fromstring(base64.b64decode(frame_model.frame), np.uint8)

        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        lbl = ["Close", "Open"]

        path = f"{path_helper.get_project_root_path()}/apps/monitoreo/ai/code"
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        count = 0
        score = 0
        thicc = 2
        rpred = [99]
        lpred = [99]

        cv2.imwrite(f"{storage_path}/image.jpg", frame)
        
        height, width = frame.shape[:2]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(
            gray, minNeighbors=5, scaleFactor=1.1, minSize=(25, 25)
        )
        left_eye = leye.detectMultiScale(gray)
        right_eye = reye.detectMultiScale(gray)

        canvas_tool["x"] = 0
        canvas_tool["y"] = 0
        canvas_tool["w"] = width
        canvas_tool["h"] = height
        canvas_tool["color"] = "black"
        tools.append(canvas_tool)
        # cv2.rectangle(
        #     frame, (0, height - 50), (200, height), (0, 0, 0), thickness=cv2.FILLED
        # )
        canvas_tool["x"] = width - 210
        canvas_tool["y"] = height - 50
        canvas_tool["w"] = width
        canvas_tool["h"] = height
        canvas_tool["color"] = "black"
        tools.append(canvas_tool)
        # cv2.rectangle(
        #     frame,
        #     (width - 210, height - 50),
        #     (width, height),
        #     (0, 0, 0),
        #     thickness=cv2.FILLED,
        # )
        for (x, y, w, h) in faces:
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 100, 100), 1)
            canvas_tool["x"] = x
            canvas_tool["y"] = y
            canvas_tool["w"] = width
            canvas_tool["h"] = height
            canvas_tool["color"] = "black"
            tools.append(canvas_tool)

        for (x, y, w, h) in right_eye:
            r_eye = frame[y : y + h, x : x + w]
            count = count + 1
            r_eye = cv2.cvtColor(r_eye, cv2.COLOR_BGR2GRAY)
            r_eye = cv2.resize(r_eye, (24, 24))
            r_eye = r_eye / 255
            r_eye = r_eye.reshape(24, 24, -1)
            r_eye = np.expand_dims(r_eye, axis=0)
            rpred = model.predict(r_eye)[0]

            if round(rpred[0]) == 1:
                lbl = "Open"
            if round(rpred[0]) == 0:
                lbl = "Closed"
            break
        for (x, y, w, h) in left_eye:
            l_eye = frame[y : y + h, x : x + w]
            count = count + 1
            l_eye = cv2.cvtColor(l_eye, cv2.COLOR_BGR2GRAY)
            l_eye = cv2.resize(l_eye, (24, 24))
            l_eye = l_eye / 255
            l_eye = l_eye.reshape(24, 24, -1)
            l_eye = np.expand_dims(l_eye, axis=0)
            lpred = model.predict(l_eye)[0]
            # print(round(lpred[0]))

            if round(lpred[0]) == 1:
                lbl = "Open"
            if round(lpred[0]) == 0:
                lbl = "Closed"
            break
        if round(rpred[0]) == 1 and round(lpred[0]) == 1:
            lbl = "Closed"
            score = score + 1
            canvas_tool["type"] = "text"
            canvas_tool["x"] = width - 210
            canvas_tool["y"] = height - 50
            canvas_tool["w"] = width
            canvas_tool["h"] = height
            canvas_tool["color"] = "black"
            canvas_tool["text"] = lbl
            tools.append(canvas_tool)

            # cv2.putText(
            #     frame, "Closed", (10, height - 20), font, 1, (255, 255, 255), 1, cv2.LINE_AA
            # )
        else:
            score = score - 1
            lbl = "Open"
            canvas_tool["type"] = "text"
            canvas_tool["x"] = width - 210
            canvas_tool["y"] = height - 50
            canvas_tool["w"] = width
            canvas_tool["h"] = height
            canvas_tool["color"] = "black"
            canvas_tool["text"] = lbl
            tools.append(canvas_tool)
            # cv2.putText(
            #     frame, "Open", (10, height - 20), font, 1, (255, 255, 255), 1, cv2.LINE_AA
            # )
        if score < 0:
            score = 0

        canvas_tool["type"] = "text"
        canvas_tool["x"] = width - 210
        canvas_tool["y"] = height - 50
        canvas_tool["w"] = width
        canvas_tool["h"] = height
        canvas_tool["color"] = "black"
        canvas_tool["text"] = "Score:" + str(score)
        tools.append(canvas_tool)
        # cv2.putText(
        #     frame,
        #     "Score:" + str(score),
        #     (100, height - 20),
        #     font,
        #     1,
        #     (255, 255, 255),
        #     1,
        #     cv2.LINE_AA,
        # )
        canvas_tool["type"] = "text"
        canvas_tool["x"] = width - 210
        canvas_tool["y"] = height - 50
        canvas_tool["w"] = width
        canvas_tool["h"] = height
        canvas_tool["color"] = "black"
        canvas_tool["text"] = "Left Eye:" + str(round(lpred[0], 2))
        tools.append(canvas_tool)
        cv2.putText(
            frame,
            "Press q to EXIT",
            (width - 200, height - 20),
            font,
            1,
            (255, 255, 255),
            1,
            cv2.LINE_AA,
        )
        if score > 5:
            # person is feeling sleepy so we beep the alarm
            cv2.imwrite(f"{storage_path}/image.jpg", frame)

            try:
                #sound.play()

                #HERE MUST SEND A NOTIFICATION TO THE USER
                data["action"]="RESET"
                print("Drowsy")

            except:  # isplaying = False
                pass

            if thicc < 16:
                thicc = thicc + 2
            else:
                thicc = thicc - 2
                if thicc < 2:
                    thicc = 2
            cv2.rectangle(frame, (0, 0), (width, height), (0, 0, 255), thicc)
            cv2.imwrite(f"{storage_path}/image.jpg", frame)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            pass

        cv2.destroyAllWindows()

        data["image"] = f"{APP_URL}/media/monitoreo/image.jpg"
        # Return a JsonResponse with the result
        data["tools"]=tools
        return data
