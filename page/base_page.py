from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as CService
from selenium.webdriver.firefox.service import Service as FService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class BasePageClass:

    def __init__(self, url, browser, device):

        self._url = url
        self._browser = browser
        self.links = {}

        if browser == "firefox":
            self._driver = webdriver.Firefox(service=FService(GeckoDriverManager().install()))
        else:
            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_settings.geolocation": 2}
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument('--disable-notifications')
            chrome_options.add_argument('disable-geolocation')
            chrome_options.add_argument('--disable-infobars')
            chrome_options.add_experimental_option("prefs", prefs)

            if device == "mobile":
                device_opt = {"deviceName": "Pixel 5"}
                chrome_options.add_experimental_option("mobileEmulation", device_opt)

            self._driver = webdriver.Chrome(service=CService(ChromeDriverManager().install()), options=chrome_options)

        self._driver.maximize_window()
        self._driver.implicitly_wait(5)
        self._driver.get(url)
        self._wait = WebDriverWait(self._driver, 5)
        self._base_handler = self._driver.current_window_handle

    def check_element(self, selector):
        try:
            el = self._wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, selector)))
            return True
        except Exception as ex:
            return False

    def element_is_visible(self, selector):
        try:
            el = self._wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, selector)))
            return el
        except Exception as ex:
            return ex

    def element_is_clickable(self, selector, xpath=None):
        try:
            if xpath is not None:
                el = self._wait.until(expected_conditions.element_to_be_clickable((By.XPATH, selector)))
            else:
                el = self._wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, selector)))
            return el
        except Exception as ex:
            return ex

    def get_element_url(self, selector, xpath=None):
        try:
            if xpath is not None:
                el = self._wait.until(expected_conditions.element_to_be_clickable((By.XPATH, selector)))
            else:
                el = self._wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, selector)))
            return el.get_attribute('href')
        except Exception as ex:
            return ""

    def click(self, selector, xpath=None):
        if xpath is not None:
            el = self._wait.until(expected_conditions.element_to_be_clickable((By.XPATH, selector)))
        else:
            el = self._wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        el.click()

    def next_tab(self):
        for w in self._driver.window_handles:
            if w != self._base_handler:
                self._driver.switch_to.window(w)

    def check_page_url(self, url):
        try:
            checker = self._wait.until(expected_conditions.url_contains(url))
            return checker
        except Exception as ex:
            return False

    def close_current_tab(self):
        self._driver.close()
        self._driver.switch_to.window(self._base_handler)

    def get_location(self, selector=None):
        if selector is None:
            return self._driver.execute_script("return window.pageYOffset")
        else:
            try:
                el = self._wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, selector)))
                self._driver.execute_script("arguments[0].scrollIntoView();", el)
                location = self._driver.execute_script("return window.pageYOffset")
                return location
            except Exception as ex:
                return None

    def click_svg(self, selector):
        svg_path = '//' + '[@'.join(selector.split('[')) + '//*[name()=\'svg\']'
        el = self._driver.find_element(By.XPATH, svg_path)
        el.click()

    def to_main_page(self):
        self._driver.get(self._url)

    def __del__(self):
        self._driver.quit()
