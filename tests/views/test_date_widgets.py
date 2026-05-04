import pytest
from pages.home_page import HomePage
from pages.views.date_widgets_page import DateWidgetPage
from pages.views.views_home_page import ViewsHomePage


class TestDateWidget:

    @pytest.mark.date
    def test_date_setting(self, driver):
        homepage = HomePage(driver)

        homepage.navigate_to('Views')

        views = ViewsHomePage(driver)
        views.navigate_to('Date Widgets')

        date_page = DateWidgetPage(driver)

        set_date = "1-1-2020"
        date_page.set_date_to(set_date)

        current_date = date_page.confirm_date_time()[0]

        assert current_date == set_date, 'Set date and Current date did not match'

    @pytest.mark.time
    def test_dialer_time_setting(self, driver):
        homepage = HomePage(driver)

        homepage.navigate_to('Views')

        views = ViewsHomePage(driver)
        views.navigate_to('Date Widgets')

        date_page = DateWidgetPage(driver)

        set_time = "1-10-pm"
        date_page.set_dialer_time_to(set_time)

        current_time = date_page.confirm_date_time()[1]

        assert current_time == set_time, 'Set time and Current time did not match'

