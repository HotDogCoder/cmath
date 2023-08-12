from apps.monitoreo.domain.models.alira import Alira
from apps.monitoreo.domain.models.screenshot import Screenshot
from apps.monitoreo.presentation.controllers.alira_controller import AliraController
from apps.monitoreo.presentation.controllers.screenshot_controller import ScreenshotController


class AliraPage():

    def __init__(self):
        pass

    @staticmethod
    def set_seo_parameters_per_page(e):
        driver = 'Chrome'
        image_name_prefix = 'alira_'

        alira = Alira(
            url="https://gms-internacional.pre.tecnalis.com/alira-server/login.jsp",
            image_name_prefix=image_name_prefix,
            driver=driver,
            alira_helper=None
        )

        AC = AliraController()
        AC.set_seo_parameters_per_page(alira=alira)
        pass

    @staticmethod
    def set_seo_redirection(e):
        driver = 'Chrome'
        image_name_prefix = 'alira_'

        alira = Alira(
            url="https://gms-internacional.pre.tecnalis.com/alira-server/login.jsp",
            image_name_prefix=image_name_prefix,
            driver=driver,
            alira_helper=None
        )

        AC = AliraController()
        AC.set_seo_redirection(alira=alira)
        pass

    @staticmethod
    def take_screenshot_of_servers_status_1(e):

        driver = 'Chrome'
        image_name_prefix = 'screenshot_'

        screenshot = Screenshot(
            url="https://demo-acp.calimaco.com/",
            image_name_prefix=image_name_prefix,
            driver=driver
        )

        SC = ScreenshotController()
        SS = SC.take_screenshot_of_servers_status_1(screenshot=screenshot)

        print('------------- termino -----------------')
        print(SS.image_list)
        pass
