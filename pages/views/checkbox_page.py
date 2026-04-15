from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)


class CheckboxPage(BasePage):
    # ── Locators ───────────────────────────────────

    CHECKBOX_1 = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Checkbox 1")'
    )

    CHECKBOX_2 = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Checkbox 2")'
    )

    # ── Actions ────────────────────────────────────

    def select_checkbox_1(self):
        logger.info("Selecting Checkbox 1")

        self.click(self.CHECKBOX_1)

    def select_checkbox_2(self):
        logger.info("Selecting Checkbox 2")

        self.click(self.CHECKBOX_2)

        # ── Verifications ──────────────────────────────

    def is_checkbox_1_selected(self):
        return self.find_visible_element(self.CHECKBOX_1).is_selected()

    def is_checkbox_2_selected(self):
        return self.find_visible_element(self.CHECKBOX_2).is_selected()