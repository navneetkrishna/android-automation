from pages.home_page import HomePage
from pages.views.controls_page import ControlsPage
from pages.views.views_home_page import ViewsHomePage


class TestCheckbox:

    def test_checkbox_selection(self, driver):
        # Main Menu → Views
        home = HomePage(driver)
        home.navigate_to("Views")

        # Views → Controls → Checkbox
        views = ViewsHomePage(driver)
        views.navigate_to("Controls")

        views.navigate_to("1. Light Theme")

        # controls page
        controls = ControlsPage(driver)

        # checkbox validation
        controls.select_checkbox_1()
        assert controls.is_checkbox_1_selected()

        controls.select_checkbox_2()
        assert controls.is_checkbox_2_selected()

    def test_radio_selection(self, driver):
        # Main Menu → Views
        home = HomePage(driver)
        home.navigate_to("Views")

        # Views → Controls → Radio
        views = ViewsHomePage(driver)
        views.navigate_to("Controls")
        views.navigate_to("1. Light Theme")

        # controls page
        controls = ControlsPage(driver)

        # radio button validation
        controls.select_radio1()
        assert controls.is_radio_1_selected()

        controls.select_radio2()
        assert controls.is_radio_2_selected()

    # def test_dropdown_selection(self, driver):
    #     # Main Menu → Views
    #     home = HomePage(driver)
    #     home.navigate_to("Views")
    #
    #     # Views → Controls → Radio
    #     views = ViewsHomePage(driver)
    #     views.navigate_to("Controls")
    #     views.navigate_to("1. Light Theme")
    #
    #     # controls page
    #     controls = ControlsPage(driver)
    #
    #     controls.click_dropdown()
