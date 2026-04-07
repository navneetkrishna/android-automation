from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)


class HomePage(BasePage):
    # Locators
    MENU_LIST = (AppiumBy.CLASS_NAME, "android.widget.TextView")

    def menu_item(self, name):
        return (
            AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{name}")'
        )

    def navigate_to(self, menu_name):
        logger.info(f"Navigating to menu: {menu_name}")
        self.scroll_to_text(menu_name)
        self.click(self.menu_item(menu_name))


    def get_all_menu_items(self):
        items = self.find_all_elements(self.MENU_LIST)
        return [item.text for item in items if item.text]

