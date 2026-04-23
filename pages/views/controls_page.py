from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from utils.logger import get_logger

logger = get_logger(__name__)


class ControlsPage(BasePage):
    # ── Locators ───────────────────────────────────
    CHECKBOX_1 = (
        AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Checkbox 1")')

    CHECKBOX_2 = (
        AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Checkbox 2")')

    RADIO_1 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("RadioButton 1")')

    RADIO_2 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("RadioButton 2")')


    # ── Actions ────────────────────────────────────
    def select_checkbox_1(self):
        logger.info("Selecting Checkbox 1")
        self.click(self.CHECKBOX_1)

    def select_checkbox_2(self):
        logger.info("Selecting Checkbox 2")
        self.click(self.CHECKBOX_2)

    def select_radio1(self):
        logger.info("Selecting Checkbox 1")
        self.click(self.RADIO_1)

    def select_radio2(self):
        logger.info("Selecting Checkbox 1")
        self.click(self.RADIO_2)


    # ── Verifications ──────────────────────────────

    def is_checkbox_1_selected(self):
        return self.find_visible_element(self.CHECKBOX_1).get_attribute('checked') == 'true'

    def is_checkbox_2_selected(self):
        return self.find_visible_element(self.CHECKBOX_2).get_attribute('checked') == 'true'

    def is_radio_1_selected(self):
        return self.find_visible_element(self.RADIO_1).get_attribute('checked') == 'true'

    def is_radio_2_selected(self):
        return self.find_visible_element(self.RADIO_2).get_attribute('checked') == 'true'
