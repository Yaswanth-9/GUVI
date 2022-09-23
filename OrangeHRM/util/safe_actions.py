import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC


class SafeActions():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def safe_check_for_element(self, locator, locator_name):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
        except NoSuchElementException:
            print(f'{locator_name} not found')
        except TimeoutException:
            print(f'{locator_name} not found with in time')
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
        except StaleElementReferenceException:
            print(f'Staleness found for {locator_name}')
        except ElementNotVisibleException:
            print(f'{locator_name} not visible on UI')
        print(f'{locator_name} found -- Proceeding to further')

    def safe_click(self, locator, locator_name):
        self.safe_check_for_element(locator=locator, locator_name=locator_name)
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
        except ElementNotInteractableException:
            print(f'{locator_name} not interactable')
        except TimeoutException:
            print(f'{locator_name} not clickable')
        ele = self.driver.find_element(*locator)
        self.set_high_light(ele, "red", 2)
        ele.click()
        print(f'Clicked on {locator_name}')

    def safe_type(self, locator, text, locator_name):
        self.safe_check_for_element(locator=locator, locator_name=locator_name)
        ele = self.driver.find_element(*locator)
        self.set_high_light(ele, "red", 2)
        ele.send_keys(text)
        print(f'sent text "{text}" to {locator_name}')

    def safe_select_from_dropdown(self, locator, value, locator_name):
        self.safe_check_for_element(locator=locator, locator_name=locator_name)
        ele = self.driver.find_element(*locator)
        self.set_high_light(ele, "red", 2)
        select_value = Select(ele)
        select_value.select_by_value(value)

    def safe_wait_until_element_not_found(self, locator, locator_name):
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
            print(f'{locator_name} not found -- Proceeding to further')
        except:
            print(f'{locator_name} found')

    def safe_get_text(self, locator, locator_name):
        self.safe_check_for_element(locator=locator, locator_name=locator_name)
        ele = self.driver.find_element(*locator)
        self.set_high_light(ele, "green", 2)
        return ele.text

    def safe_handle_alert(self, accept):
        try:
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            if accept:
                alert.accept()
            else:
                alert.dismiss()
        except NoAlertPresentException:
            print(f'Alert not found')

    def set_high_light(self, element, color, border):
        """Highlights (blinks) a Selenium Webdriver element"""
        driver = element._parent

        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

        original_style = element.get_attribute('style')
        apply_style("border: {0}px solid {1};".format(border, color))
        time.sleep(0.3)
        apply_style(original_style)
