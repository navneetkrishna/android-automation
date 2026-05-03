from datetime import datetime
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from utils.logger import get_logger
from utils.helpers import format_date, scroll_until_element_found
from utils import waits


logger = get_logger(__name__)


class DateWidgetPage(BasePage):

    # Locators
    DIALOG = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1. Dialog")')

    INLINE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("2. Inline")')

    # Submenus

    CHANGE_THE_DATE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("io.appium.android.apis:id/pickDate")')

    CHANGE_THE_TIME = ( AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("io.appium.android.apis:id/pickTime")')

    CHANGE_THE_TIME_SPINNER = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("io.appium.android.apis:id/pickTimeSpinner")')

    CALENDAR_OK = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/button1")')


    # Actions

    def click_dialog_option(self):
        logger.info("Clicking Dialog button")
        self.click(self.DIALOG)

    def click_inline_option(self):
        logger.info("Clicking Inline button")
        self.click(self.DIALOG)

    def set_date_to(self, set_date:str):
        logger.info(f"Setting date to {set_date}")

        f_date = format_date(set_date).split('-')
        print(f_date)

        # navigate to Dialog >> 'change the date'
        self.click_dialog_option()

        logger.info("Clicking 'change the date' button")
        self.click(self.CHANGE_THE_DATE)

        # change date >> month >> year

        # 1. select date
        logger.info(f"Selecting date: {f_date[0]}")
        waits.wait_visible(self.driver, (AppiumBy.ANDROID_UIAUTOMATOR,
                            f'new UiSelector().text("{f_date[0]}")')
                           ).click()

        # 2. select month


        # 3. select year
        # open year dropdown
        logger.info('Clicking year dropdown')
        waits.wait_visible(self.driver, (AppiumBy.ANDROID_UIAUTOMATOR,
                            f'new UiSelector().resourceId("android:id/date_picker_header_year")')
                           ).click()

        current_year = int(datetime.today().year)
        logger.info(f"Current year: {current_year}, searching for year: {f_date[2]}")

        # dynamic locator to locate a year
        search_year_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{f_date[2]}")')

        if current_year < int(f_date[2]):
            scroll_until_element_found(self.driver, search_year_locator, direction='up', distance=500, timeout=2)

        else:
            scroll_until_element_found(self.driver, search_year_locator, direction='down', distance=500, timeout=2)