import subprocess
import os
from utils.logger import get_logger

logger = get_logger(__name__)


def get_connected_device_name():
    logger.info("Fetching connected Android device name via ADB...")
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    lines = result.stdout.strip().splitlines()
    devices = [line.split("\t")[0] for line in lines[1:] if "\tdevice" in line]
    if not devices:
        logger.error("No connected Android device/emulator found!")
        raise RuntimeError("No connected Android device/emulator found.")
    logger.info(f"Device found: {devices[0]}")
    return devices[0]


def get_platform_version(device_name):
    logger.info(f"Fetching Android version for device: {device_name}")
    result = subprocess.run(
        ["adb", "-s", device_name, "shell", "getprop", "ro.build.version.release"],
        capture_output=True, text=True
    )
    version = result.stdout.strip()
    logger.info(f"Platform version: {version}")
    return version


def get_device_udid():
    return get_connected_device_name()


def get_apk_path(apk_filename="MyDemoAppRN.apk"):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    apk_path = os.path.join(base_dir, "apk", apk_filename)
    if not os.path.exists(apk_path):
        logger.error(f"APK not found at: {apk_path}")
        raise FileNotFoundError(f"APK not found at: {apk_path}")
    logger.info(f"APK path resolved: {apk_path}")
    return apk_path


def get_appium_server():
    server = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
    logger.info(f"Appium server: {server}")
    return server

