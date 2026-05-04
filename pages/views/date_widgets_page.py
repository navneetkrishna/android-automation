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

    CURRENT_DATE_TIME = (AppiumBy.ID, 'io.appium.android.apis:id/dateDisplay')

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
        # print(f_date)

        # navigate to Dialog >> 'change the date'
        self.click_dialog_option()

        logger.info("Clicking 'change the date' button")
        self.click(self.CHANGE_THE_DATE)

        # change year >> month >> date

        # 1. select year
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


        # 2. select month
        logger.info('Selecting month')
        month_ele_text = self.find_element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/date_picker_header_date")')).text

        # Date format usually: "Sun, 3 May" -> Index 1 is Month
        current_month_str = month_ele_text.split(" ")[2]

        logger.info(f'Current month: {current_month_str} and target month: {f_date[1]}')

        current_month_digit = datetime.strptime(current_month_str, "%b").month
        target_month_digit = datetime.strptime(f_date[1], "%b").month

        logger.info(f'Current month numeric: {current_month_digit} and target month numeric: {target_month_digit}')

        diff = target_month_digit - current_month_digit

        if target_month_digit == current_month_digit:
            logger.info(f"target month and current month are same")
            pass

        elif diff > 0:
            for i in range(diff):
                logger.info(f"target month is higher than current month, performing next click, count: {i}")
                self.click((AppiumBy.ID, "android:id/next"))

        elif diff < 0:
            for i in range(abs(diff)):
                logger.info(f"target month is less than current month, performing prev click, count: {i}")
                self.click((AppiumBy.ID, "android:id/prev"))


        # 3. select date
        target_day = str(int(f_date[0]))
        # locator will look for "2" instead of "02"

        logger.info(f"Selecting date: {target_day}")

        day_locator = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{target_day}")')
        waits.wait_visible(self.driver, day_locator).click()
        self.click(self.CALENDAR_OK)

        def set_dialer_time_to(self, set_time:str='10-10-am'):
        logger.info(f"Setting time to {set_time}")
        self.click(self.DIALOG)
        self.click(self.CHANGE_THE_TIME)

        time_lst = [_ for _ in set_time.split('-')]
        hour, minute, segment = time_lst[0], time_lst[1], time_lst[2]

        logger.info(f"Setting hour to: {hour}, minute to: {minute} and period: {segment}")
        #     select hour >> minute >> period
        # 1. select hour
        logger.info(f"Setting hour: {hour}")

        self.click((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().description("{hour}")'))

        self.click((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().description("{minute}")'))

        self.click((AppiumBy.ID, f'android:id/{segment}_label'))

        logger.info("Time set, clicking on OK button")
        self.click(self.CALENDAR_OK)

    
    # Verification

        def confirm_date_time(self):
        logger.info(f"Confirming date and time")

        raw_text = self.find_element(self.CURRENT_DATE_TIME).text
        logger.info(f"Raw date-time text: {raw_text}")

        # App format 5-3-2026 01:02 [month-day-year 24hr-00min]

        date_part, time_part = raw_text.split(' ')
        logger.info(f"Date part: {date_part}, Time part: {time_part}")

        # Parse date
        date_obj = datetime.strptime(date_part, "%m-%d-%Y")

        # Format as Day-Month-Year (%d-%m-%Y)
        formatted_date = date_obj.strftime("%#d-%#m-%Y")
        logger.info(f"Formatted date: {formatted_date}")

        # Parse time
        time_obj = datetime.strptime(time_part, "%H:%M")

        formatted_time = time_obj.strftime("%#I-%M-%p").lower()

        logger.info(f"Formatted date: {formatted_date}")
        logger.info(f"Formatted time: {formatted_time}")

        return formatted_date, formatted_time
    
