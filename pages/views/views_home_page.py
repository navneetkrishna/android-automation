from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage

from utils.logger import get_logger

logger = get_logger(__name__)


class ViewsHomePage(BasePage):

    def menu_item(self, name):
        """

        Dynamic locator for any Views submenu item

        Example: Buttons, Checkboxes, Spinner, Lists

        """

        return (

            AppiumBy.ANDROID_UIAUTOMATOR,

            f'new UiScrollable(new UiSelector().scrollable(true))'

            f'.scrollIntoView(new UiSelector().text("{name}"))'

        )

    def navigate_to(self, submenu_name):
        logger.info(f"Navigating to Views submenu: {submenu_name}")

        self.click(self.menu_item(submenu_name))