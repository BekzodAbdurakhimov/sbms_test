import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestLogin:

    def test_login_account(self, driver):
        driver.get("https://sbms.ucell/ps/sbms/shell.html")
        wait = WebDriverWait(driver, 10)

        # checking the btn
        detail_button_check = wait.until(
            EC.visibility_of_element_located((By.ID, "details-button"))
        )
        # click the btn
        detail_button_check.click()

        print('its ok')
        go_to_link = wait.until(
            EC.visibility_of_element_located((By.ID, "proceed-link"))
        )
        go_to_link.click()
        time.sleep(3)
        login_text_locator = (By.CSS_SELECTOR, '.login-caption > span')
        login_locator_check = wait.until(EC.visibility_of_element_located(login_text_locator))
        assert login_locator_check.is_displayed(), "Nope"
        print("Locator is displayed")


        login_input_area = driver.find_element(By.CSS_SELECTOR, "input.sbms-textbox[name='user'][type='text']")
        password_input_area = driver.find_element(By.CSS_SELECTOR, "input.sbms-textbox[name='password'][type='password']")
        enter_btn = driver.find_element(By.CSS_SELECTOR, "button.sbms-button-ex")

        login_input_area.send_keys("BEKZOD.ABDURAKHIMOV")
        time.sleep(2)
        password_input_area.send_keys("Bekucell99")
        time.sleep(2)
        enter_btn.click()

