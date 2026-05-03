import pytest
from pages.home_page import HomePage
from pages.views.date_widgets_page import DateWidgetPage
from pages.views.views_home_page import ViewsHomePage
import time
from datetime import datetime

@pytest.mark.date
def test_date(driver):
    homepage = HomePage(driver)

    homepage.navigate_to('Views')

    views = ViewsHomePage(driver)
    views.navigate_to('Date Widgets')

    date_page = DateWidgetPage(driver)

    set_date = "1-1-2020"
    date_page.set_date_to(set_date)

    current_date = date_page.confirm_date()

    assert current_date == set_date, 'Set date and Current date did not match'

