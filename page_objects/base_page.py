from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  

    # Метод для ожидания URL
    def wait_for_url_contains(self, expected_url_part):
        return WebDriverWait(self.driver, 10).until(EC.url_contains(expected_url_part))
    

    # Метод для ожидания видимости элемента
    def wait_for_element_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    
    def click_element_with_wait_visible(self, locator):
        element = self.wait_element_with_wait_visible(locator)
        element.click()
    
    # Метод для ожидания кликабельности элемента
    def wait_for_element_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
    
    # Метод для клика с ожиданием кликабельности
    def click_element_with_wait_clickable(self, locator):
        element = self.wait_for_element_clickable(locator)
        element.click()

    # Метод для клика без ожидания
    def click_element(self, locator):
        return self.driver.find_element(*locator).click()
    
    # Метод для возвращения текста
    def return_text_of_element(self, locator):
        return self.driver.find_element(*locator).text
    
    # Метод для скролла до элемента
    def scroll_into_view(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    # Метод для проверки текущего URL
    def get_current_url(self):
        return self.driver.current_url
    
    def switch_window(self):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])

    def fill_field(self, locator, text):
        return self.driver.find_element(*locator).send_keys(text)

  