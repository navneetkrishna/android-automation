from pages.home_page import HomePage
from pages.views.views_home_page import ViewsHomePage
from pages.views.checkbox_page import CheckboxPage


class TestCheckbox:

    def test_checkbox_selection(self, driver):
        # Main Menu → Views
        home = HomePage(driver)
        home.navigate_to("Views")

        # Views → Controls → Checkbox
        views = ViewsHomePage(driver)
        views.navigate_to("Controls")
        views.navigate_to("Checkbox")

        # Checkbox Page
        checkbox = CheckboxPage(driver)

        checkbox.select_checkbox_1()
        assert checkbox.is_checkbox_1_selected()

        checkbox.select_checkbox_2()
        assert checkbox.is_checkbox_2_selected()