import pytest
from pages.home_page import HomePage
from pages.views.views_home_page import ViewsHomePage
from pages.views.alert_dialogs_page import AlertDialogsPage
from utils.logger import get_logger

logger = get_logger(__name__)


class TestAlertDialogs:

    @pytest.fixture(autouse=True)
    def navigate_to_alert_dialogs(self, driver):
        """Navigate to Alert Dialogs screen before each test"""
        home = HomePage(driver)
        home.navigate_to("App")

        views = ViewsHomePage(driver)
        views.navigate_to("Alert Dialogs")

        self.alert_page = AlertDialogsPage(driver)

    def test_ok_cancel_dialog_title(self, driver):
        """Verify OK/Cancel dialog opens with correct title"""
        self.alert_page.open_ok_cancel_dialog()
        title = self.alert_page.get_dialog_title()
        logger.info(f"Dialog title: {title}")
        assert title == "Lorem ipsum dolor sit aie consectetur adipiscing\nPlloaso mako nuto siwuf cakso dodtos anr koop."

    def test_accept_ok_cancel_dialog(self, driver):
        """Verify dialog closes after clicking OK"""
        self.alert_page.open_ok_cancel_dialog()
        self.alert_page.accept_dialog()
        assert not self.alert_page.is_displayed(self.alert_page.DIALOG_OK_BTN), \
            "Dialog should be dismissed after OK"

    def test_dismiss_ok_cancel_dialog(self, driver):
        """Verify dialog closes after clicking Cancel"""
        self.alert_page.open_ok_cancel_dialog()
        self.alert_page.dismiss_dialog()
        assert not self.alert_page.is_displayed(self.alert_page.DIALOG_CANCEL_BTN), \
            "Dialog should be dismissed after Cancel"

    def test_list_dialog_opens(self, driver):
        """Verify list dialog opens successfully"""
        self.alert_page.open_list_dialog()
        assert self.alert_page.is_displayed(self.alert_page.DIALOG_TITLE), \
            "List dialog should be visible"

    def test_ok_cancel_dialog_long_msg(self, driver):
        """Verify OK/Cancel dialog long title"""
        self.alert_page.open_ok_cancel_long_dialog()

        title = self.alert_page.get_dialog_message()
        logger.info(f"Dialog title: {title}")
        assert title == ("Plloaso mako nuto siwuf cakso dodtos anr koop a cupy uf cak vux noaw yerw phuno. "
                         "Whag schengos, uf efed, quiel ba mada su otrenzr."
                         "\n\nSwipontgwook proudgs hus yag su ba dagarmidad. "
                         "Plasa maku noga wipont trenzsa schengos ent kaap zux comy."
                         "\n\nWipont trenz kipg naar mixent phona. "
                         "Cak pwico siructiun ruous nust apoply tyu cak Uhex sisulutiun munityuw uw dseg")
