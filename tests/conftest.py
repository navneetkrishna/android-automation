import pytest
import os
from datetime import datetime
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.capabilities import CAPS, APPIUM_SERVER
from utils.logger import get_logger

logger = get_logger(__name__)

# ───────────────── Screenshot directory setup ─────────────────
SCREENSHOT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "reports", "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


# ───────────────── Driver Fixture ─────────────────
@pytest.fixture(scope="function")
def driver(request):
    """
    Initializes Appium driver before each test and quits after.
    Supports parallel execution via pytest-xdist (each worker gets its own driver).
    """
    logger.info(f"Starting test: {request.node.name}")
    logger.info(f"Connecting to Appium server: {APPIUM_SERVER}")

    options = UiAutomator2Options().load_capabilities(CAPS)

    try:
        driver = webdriver.Remote(APPIUM_SERVER, options=options)
        # driver.implicitly_wait(10)
        logger.info("Appium driver initialized successfully.")
    except Exception as e:
        logger.error(f"Failed to initialize Appium driver: {e}")
        raise

    yield driver

    # ───────────────── Teardown ─────────────────
    logger.info(f"Ending test: {request.node.name}")
    driver.quit()
    logger.info("Driver quit successfully.")


# ───────────────── Screenshot on Failure Hook ─────────────────
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Captures a screenshot automatically when a test FAILS.
    Attaches it to the pytest-html report.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            # Generate unique screenshot filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name.replace(" ", "_").replace("/", "_")
            screenshot_path = os.path.join(SCREENSHOT_DIR, f"FAIL_{test_name}_{timestamp}.png")

            try:
                driver.save_screenshot(screenshot_path)
                logger.warning(f"Screenshot saved: {screenshot_path}")

                # Attach to pytest-html report
                if hasattr(report, "extra"):
                    from pytest_html import extras
                    report.extra = getattr(report, "extra", [])
                    report.extra.append(extras.image(screenshot_path))

            except Exception as e:
                logger.error(f"Could not take screenshot: {e}")


# ───────────────── Logging Test Start/End ─────────────────

def pytest_runtest_logreport(report):
    if report.when == "call":
        if report.passed:
            logger.info(f"PASSED: {report.nodeid}")
        elif report.failed:
            logger.error(f"FAILED: {report.nodeid}")
        elif report.skipped:
            logger.warning(f"️SKIPPED: {report.nodeid}")