import pytest
from appium import webdriver
from time import sleep


@pytest.fixture(scope="module")
def appium_driver():
    desired_caps = {
        "platformName": "Android", 
        "platformVersion": "12.0",
        "deviceName": "emulator-5554",  
        "appPackage": "com.mytestapp", 
        "appActivity": "com.mytestapp.MainActivity", 
        "automationName": "UiAutomator2", 
        "noReset": True 
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()


def test_launch_app_and_click_button(appium_driver):
    driver = appium_driver

    # Verify the app launched
    assert driver.is_app_installed("com.mytestapp"), "MyTestApp is not installed!"
    print("MyTestApp launched successfully!")

    # Locate a button and click it
    try:
        button = driver.find_element_by_id("com.mytestapp:id/startButton") 
        button.click()
        print("Start button clicked successfully!")
    except Exception as e:
        pytest.fail(f"Failed to interact with the start button: {e}")

    sleep(2)
