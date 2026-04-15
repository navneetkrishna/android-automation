from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)


class ButtonsPage(BasePage):
    # ── Locators ───────────────────────────────────

    NORMAL_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Normal")'
    )

    SMALL_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Small")'
    )

    TOGGLE_BUTTON = (
        AppiumBy.CLASS_NAME,
        "android.widget.ToggleButton"
    )

    # ── Actions ────────────────────────────────────

    def click_normal_button(self):
        logger.info("Clicking Normal button")

        self.click(self.NORMAL_BUTTON)

    def click_small_button(self):
        logger.info("Clicking Small button")

        self.click(self.SMALL_BUTTON)

    def toggle_button(self):
        logger.info("Toggling button")

        self.click(self.TOGGLE_BUTTON)

        # ── Verifications ──────────────────────────────

    def is_normal_button_displayed(self):
        return self.is_displayed(self.NORMAL_BUTTON)