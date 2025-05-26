from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_product_list_display(browser):
    # Step 1: Open login page and log in with valid credentials
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    # Step 2: Wait until the inventory page loads (URL contains /inventory.html)
    WebDriverWait(browser, 5).until(
        EC.url_contains("/inventory.html")
    )

    # Step 3: Verify at least one product item is visible on the page
    products = browser.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0, "No products found on inventory page"

    # Optionally, print product names (for your reference)
    for product in products:
        name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        print(f"Product found: {name}")
