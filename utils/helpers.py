import subprocess
import os
from datetime import datetime

from selenium.common import NoSuchElementException

from utils.logger import get_logger
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput
from utils.waits import wait_visible, wait_clickable, wait_all_visible, presence_located

logger = get_logger(__name__)


def get_connected_device_name():
    logger.info("Fetching connected Android device name via ADB...")
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    lines = result.stdout.strip().splitlines()
    devices = [line.split("\t")[0] for line in lines[1:] if "\tdevice" in line]
    if not devices:
        logger.error("No connected Android device/emulator found!")
        raise RuntimeError("No connected Android device/emulator found.")
    logger.info(f"Device found: {devices[0]}")
    return devices[0]


def get_platform_version(device_name):
    logger.info(f"Fetching Android version for device: {device_name}")
    result = subprocess.run(
        ["adb", "-s", device_name, "shell", "getprop", "ro.build.version.release"],
        capture_output=True, text=True
    )
    version = result.stdout.strip()
    logger.info(f"Platform version: {version}")
    return version


def get_device_udid():
    return get_connected_device_name()


def get_apk_path(apk_filename="MyDemoAppRN.apk"):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    apk_path = os.path.join(base_dir, "apk", apk_filename)
    if not os.path.exists(apk_path):
        logger.error(f"APK not found at: {apk_path}")
        raise FileNotFoundError(f"APK not found at: {apk_path}")
    logger.info(f"APK path resolved: {apk_path}")
    return apk_path


def get_appium_server():
    server = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
    logger.info(f"Appium server: {server}")
    return server


def format_date(set_date:str):
    logger.info(f"Formatting date: {set_date}")
    # 1. Parse the string into a datetime object
    # %d: day, %m: numeric month, %Y: 4-digit year
    date_obj = datetime.strptime(set_date, "%d-%m-%Y")

    # 2. Format the object back into a string
    # %b: abbreviated month name (e.g., Dec)
    formatted_date = date_obj.strftime("%d-%b-%Y")

    logger.info(f"Formatted date: {formatted_date}")
    # print(formatted_date)
    return formatted_date


def get_touch_actions(driver, pointer_count: int = 1):
    """
    Utility to instantiate ActionBuilder with pre-configured touch pointers.
    """
    actions = ActionBuilder(driver)

    # Override the default mouse pointer and add touch pointers
    actions.devices = []

    for i in range(pointer_count):
        # Create a unique PointerInput for each finger
        finger = PointerInput(interaction.POINTER_TOUCH, f"finger{i}")
        actions.devices.append(finger)

    return actions


def perform_scroll(driver, element=None, direction="up", distance=500):
    """
    Performs a scroll. If an element is provided, it scrolls starting from that element.
    Otherwise, it scrolls from the center of the screen.
    """
    # 1. Initialize Touch Device using utility.get_touch_actions
    actions = get_touch_actions(driver, pointer_count=1)
    finger = actions.devices[0]

    # 2. Determine Start Point (x, y)
    if not element:
        # Get screen center coordinates
        size = driver.get_window_size()
        start_x = size['width'] / 2
        start_y = size['height'] / 2
        logger.info(f"Scrolling from screen center at {start_x}, {start_y}")

    else:
        # Get element center coordinates
        rect = element.rect
        start_x = rect['x'] + (rect['width'] / 2)
        start_y = rect['y'] + (rect['height'] / 2)
        logger.info(f"Scrolling from element at {start_x}, {start_y}")

    # 3. Calculate End Point based on direction
    end_x = start_x
    if direction == "up":
        end_y = start_y - distance
    else:  # down
        end_y = start_y + distance

    # 4. Record the Sequence (Move -> Down -> Move -> Up)
    # Start at the point (no duration)
    finger.create_pointer_move(duration=0, x=start_x, y=start_y)
    # finger.create_pointer_down(interaction.PointerContact.LEFT)
    finger.create_pointer_down()

    # Smooth move to the end point (duration creates the 'swipe' feel)
    finger.create_pointer_move(duration=600, x=end_x, y=end_y)

    # Release the finger
    finger.create_pointer_up(button=0)

    # 5. Perform the recorded sequence
    actions.perform()


def scroll_until_element_found(driver, locator, direction="up", distance=500, timeout=10, max_scrolls=10):
    logger.info(f"Scrolling until element found with max scrolls {max_scrolls} and timeout {timeout}")
    # max_scrolls = 10  # Safety break to prevent infinite loops
    scroll_count = 0

    while scroll_count < max_scrolls:
        try:
            element = presence_located(driver, locator, timeout)
            # Check if the year is already visible before scrolling
            if element:
                element.click()
                logger.info(f"Element found, returning element")
                # Exit function entirely
                return  element

        except NoSuchElementException, TimeoutError:
            # If not found or not clickable, scroll and try again
            logger.info(f"Element is not visible, performing scroll {scroll_count + 1}")
            perform_scroll(driver, direction=direction, distance=distance)
            scroll_count += 1

    # If we exit the loop, the element was never found
    raise TimeoutError(f"Could not find element after {max_scrolls} scrolls.")