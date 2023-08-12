from apps.alira.domain.models.screenshot import Screenshot
from apps.alira.presentation.controllers.screenshot_controller import ScreenshotController

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

