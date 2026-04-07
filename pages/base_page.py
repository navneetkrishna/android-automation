from appium.webdriver.common.appiumby import AppiumBy
from utils.waits import wait_visible, wait_clickable, wait_all_visible, presence_located
from utils.logger import get_logger

logger = get_logger(__name__)


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        """Find element using presence (exists in DOM, may not be visible)"""
        logger.debug(f"Finding element: {locator}")
        return presence_located(self.driver, locator)

    def find_visible_element(self, locator):
        """Find element that is visible on screen"""
        logger.debug(f"Finding visible element: {locator}")
        return wait_visible(self.driver, locator)

    def find_clickable_element(self, locator):
        """Find element that is visible and clickable"""
        logger.debug(f"Finding clickable element: {locator}")
        return wait_clickable(self.driver, locator)

    def find_all_elements(self, locator):
        """Find all visible elements matching the locator"""
        logger.debug(f"Finding all elements: {locator}")
        return wait_all_visible(self.driver, locator)

    def click(self, locator):
        logger.info(f"Clicking element: {locator}")
        self.find_clickable_element(locator).click()

    def enter_text(self, locator, text):
        logger.info(f"Entering text '{text}' into {locator}")
        element = self.find_visible_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        text = self.find_visible_element(locator).text
        logger.debug(f"Got text: '{text}' from {locator}")
        return text

    def is_displayed(self, locator):
        try:
            return self.find_visible_element(locator).is_displayed()
        except Exception:
            return False

    def scroll_to_text(self, text):
        """Scroll until element with given text is visible — UiAutomator2"""
        logger.info(f"Scrolling to text: '{text}'")
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true))'
            f'.scrollIntoView(new UiSelector().text("{text}"))'
        )

    def navigate_back(self):
        logger.info("Navigating back")
        self.driver.back()