import random

from jinja2.nodes import And

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

    DROPDOWN_LIST = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/select_dialog_listview")')

    CURRENT_DROPDOWN_ITEM = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/text1")')


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
        self.select_dropdown()

        # 2. Handle 'None' or validate the choice
        if option is None:
            option = random.choice(ControlsPage.DROPDOWN_MENU_ITEMS)
            logger.info(f"Randomly picked: {option}")

        elif option not in ControlsPage.DROPDOWN_MENU_ITEMS:
            logger.error(f"Option '{option}' is not a valid option!")
            return None

        # 3. Select the option
        logger.info(f"Clicking on option text: {option}")
        self.click((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{option}")'))

        return option

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
        return self.find_visible_element(self.DROPDOWN_LIST).is_displayed()

    def selected_dropdown_option(self):
        logger.info("Selected dropdown option")
        return self.find_visible_element(self.CURRENT_DROPDOWN_ITEM).get_attribute('text')
