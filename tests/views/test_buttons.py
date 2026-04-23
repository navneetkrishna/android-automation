import pytest

from pages.home_page import HomePage
from pages.views.views_home_page import ViewsHomePage
from pages.views.buttons_page import ButtonsPage


class TestButtons:

    def test_normal_button_click(self, driver):

        # Main Menu → Views
        home = HomePage(driver)
        home.navigate_to("Views")

        # Views → Buttons
        views = ViewsHomePage(driver)
        views.navigate_to("Buttons")

        # Buttons actions
        buttons = ButtonsPage(driver)
        assert buttons.is_normal_button_displayed()
        buttons.click_normal_button()

    def test_small_button_click(self, driver):

        # Main Menu → Views
        home = HomePage(driver)
        home.navigate_to("Views")

        # Views → Buttons
        views = ViewsHomePage(driver)
        views.navigate_to("Buttons")

        # Buttons actions
        buttons = ButtonsPage(driver)

        assert buttons.is_small_button_displayed()
        buttons.click_small_button()


    @pytest.mark.demo
    def test_toggle_button(self, driver):

        # Main Menu → Views
        home = HomePage(driver)
        home.navigate_to("Views")

        # Views → Buttons
        views = ViewsHomePage(driver)
        views.navigate_to("Buttons")

        # Buttons actions
        buttons = ButtonsPage(driver)


        # initial toggle button state is OFF
        buttons.click_toggle_button()

        assert buttons.toggle_button_status() == 'ON'
