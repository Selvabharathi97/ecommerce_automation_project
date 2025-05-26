from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_login_valid(browser):
    browser.get("https://www.saucedemo.com/")

    # Enter valid username and password
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    # Wait for URL to change indicating successful login
    WebDriverWait(browser, 5).until(
        EC.url_contains("/inventory.html")
    )

    # Assert current URL contains /inventory.html to confirm login success
    assert "/inventory.html" in browser.current_url


def test_login_invalid_password(browser):
    # Load the site
    browser.get("https://www.saucedemo.com/")

    # Enter invalid username and password
    browser.find_element(By.ID, "user-name").send_keys("valid_user@example.com")
    browser.find_element(By.ID, "password").send_keys("wrong_password")
    browser.find_element(By.ID, "login-button").click()

    # Wait for the error message element to be visible
    error_element = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )

    # Assert the exact error message text
    assert error_element.text == "Epic sadface: Username and password do not match any user in this service"
