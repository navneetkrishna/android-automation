from utils.helpers import (
    get_connected_device_name,
    get_platform_version,
    get_appium_server
)

device = get_connected_device_name()

CAPS = {
    "platformName": "Android",
    "appium:deviceName": device,
    "appium:udid": device,
    "appium:platformVersion": get_platform_version(device),
    "appium:app": "D:/QA_Automation/android-automation/apk/ApiDemos-debug.apk",
    "appium:automationName": "UiAutomator2",
    "appium:appWaitActivity": "*",
    "appium:noReset": False,
    "appium:newCommandTimeout": 120
}

APPIUM_SERVER = get_appium_server()