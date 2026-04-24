import random

from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from utils.logger import get_logger

logger = get_logger(__name__)


class ControlsPage(BasePage):

    DROPDOWN_MENU_ITEMS = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

    # ── Locators ───────────────────────────────────

    CHECKBOX_1 = (
        AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Checkbox 1")')

    CHECKBOX_2 = (
        AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Checkbox 2")')

    RADIO_1 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("RadioButton 1")')

    RADIO_2 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("RadioButton 2")')

    DROPDOWN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("io.appium.android.apis:id/spinner1")')

    DROPDOWN_MENU = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/select_dialog_listview")')


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

    def select_dropdown(self):
        logger.info("Selecting dropdown")
        self.click(self.DROPDOWN)

    def select_dropdown_menu_option(self, option=None):
        # 1. Open the dropdown first
        logger.info("Opening dropdown menu")
        self.click(ControlsPage.DROPDOWN)

        # 2. Handle 'None' or validate the choice
        if option is None:
            option = random.choice(ControlsPage.DROPDOWN_MENU_ITEMS)
            logger.info(f"Randomly picked: {option}")

        elif option not in ControlsPage.DROPDOWN_MENU_ITEMS:
            logger.error(f"Option '{option}' is not a valid planet!")
            return None

        # 3. Select the option
        logger.info(f"Clicking on option text: {option}")
        # Tip: Using UiSelector().text() is perfect here for precision
        self.click((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{option}")'))

        return option

    # def select_dropdown_menu_option(self, option=None):
    #
    #     logger.info(f"Received dropdown menu option: {option}")
    #
    #     if option is None:
    #         logger.info(f"None passed as desired option, picking a random option from the options list")
    #
    #         option = random.choice(ControlsPage.DROPDOWN_MENU_ITEMS)
    #         logger.info(f"Picked option from the options list: {option}")
    #
    #         logger.info(f"Selecting option: {option}")
    #         self.click((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{option}")'))
    #
    #         return option
    #
    #     elif option in ControlsPage.DROPDOWN_MENU_ITEMS:
    #         logger.info(f"Selecting option: {option}")
    #         self.click((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{option}")'))
    #
    #         return option
    #
    #     return None

    # ── Verifications ──────────────────────────────

    def is_checkbox_1_selected(self):
        return self.find_visible_element(self.CHECKBOX_1).get_attribute('checked') == 'true'

    def is_checkbox_2_selected(self):
        return self.find_visible_element(self.CHECKBOX_2).get_attribute('checked') == 'true'

    def is_radio_1_selected(self):
        return self.find_visible_element(self.RADIO_1).get_attribute('checked') == 'true'

    def is_radio_2_selected(self):
        return self.find_visible_element(self.RADIO_2).get_attribute('checked') == 'true'

    def is_dropdown_opened(self):
        return self.find_visible_element(self.DROPDOWN_MENU).is_displayed()

    def selected_dropdown_option(self):
        logger.info("Selected dropdown option")
