from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)

class AlertDialogsPage(BasePage):

    # ── Locators ─────────────────────────────────────────────────────────────
    # Alert Dialog Buttons (main list)
    OK_CANCEL_DIALOG_BTN    = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OK CANCEL DIALOG WITH A MESSAGE")')
    OK_CANCEL_LONG_BTN      = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("OK CANCEL DIALOG WITH A LONG MESSAGE")')
    LIST_DIALOG_BTN         = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("LIST DIALOG")')
    PROGRESS_DIALOG_BTN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("PROGRESS DIALOG")')
    SINGLE_CHOICE_BTN       = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("SINGLE CHOICE LIST")')
    MULTI_CHOICE_BTN        = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("REPEAT ALARM")')

    # ── Dialog Action Buttons ─────────────────────────────────────────────────
    DIALOG_OK_BTN           = (AppiumBy.ID, "android:id/button1")
    DIALOG_CANCEL_BTN       = (AppiumBy.ID, "android:id/button2")
    DIALOG_TITLE            = (AppiumBy.ID, "android:id/alertTitle")
    DIALOG_MESSAGE          = (AppiumBy.ID, "android:id/message")

    # ── Actions ───────────────────────────────────────────────────────────────
    def open_ok_cancel_dialog(self):
        logger.info("Opening OK/Cancel dialog")
        self.click(self.OK_CANCEL_DIALOG_BTN)

    def get_dialog_title(self):
        return self.get_text(self.DIALOG_TITLE)

    def get_dialog_message(self):
        return self.get_text(self.DIALOG_MESSAGE)

    def accept_dialog(self):
        logger.info("Accepting dialog (OK)")
        self.click(self.DIALOG_OK_BTN)

    def dismiss_dialog(self):
        logger.info("Dismissing dialog (Cancel)")
        self.click(self.DIALOG_CANCEL_BTN)

    def open_list_dialog(self):
        logger.info("Opening List dialog")
        self.click(self.LIST_DIALOG_BTN)

    def open_single_choice_dialog(self):
        logger.info("Opening Single Choice dialog")
        self.click(self.SINGLE_CHOICE_BTN)

    def open_progress_dialog(self):
        logger.info("Opening Progress dialog")
        self.click(self.PROGRESS_DIALOG_BTN)

    def open_ok_cancel_long_dialog(self):
        logger.info("Opening OK/Cancel long dialog")
        self.click(self.OK_CANCEL_LONG_BTN)
