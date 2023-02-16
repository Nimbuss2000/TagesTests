import pytest
import allure
from configs.config import base_url
from helpers.tests_data import TestData


@allure.epic("Links")
@allure.story("Page links validation")
class TestLinksClickable:
    """Group of tests for check main page links"""

    test_naming = 'links_tests'
    test_data = TestData().get_sections(test_naming)

    @pytest.mark.mobile
    @pytest.mark.run(order=1)
    def test_burger_clickable(self, work_driver):
        work_driver.to_main_page()
        selector = ".header__burger"

        element = work_driver.element_is_clickable(selector)
        assert not isinstance(element, Exception), "Element is not clickable"

    @pytest.mark.mobile
    @pytest.mark.order(order=2)
    @pytest.mark.parametrize('name, data', test_data['static_header_mobile'].items())
    def test_static_header_links_mobile(self, work_driver, get_status_code, name, data):
        work_driver.to_main_page()
        burger_selector = ".header__burger"

        work_driver.click(burger_selector)

        element = work_driver.element_is_clickable(data['selector'], xpath=True)
        assert not isinstance(element, Exception), "Element is not clickable"

        element_url = work_driver.get_element_url(data['selector'], xpath=True)
        assert element_url == ''.join([base_url, data['href']]), "Element url is note matched with expected url"

        status_code = get_status_code(element_url)
        assert status_code == 200, "Url have bad response"

        work_driver.click(data['selector'], xpath=True)
        url = work_driver.check_page_url(element_url)
        assert url, "Click on element dont open expected page"

    @allure.title("Header links")
    @pytest.mark.desktop
    @pytest.mark.parametrize('name, data', test_data['static_header'].items())
    def test_static_header_links_desktop(self, work_driver, get_status_code, name, data):
        """Test:
        1) Element is clickable
        2) Link in element match to expect link
        3) Link request is valid
        4) Click on the element open link"""

        work_driver.to_main_page()

        element = work_driver.element_is_clickable(data['selector'])
        assert not isinstance(element, Exception), "Element not available"

        element_url = work_driver.get_element_url(data['selector'])
        assert element_url == ''.join([base_url, data['href']]), "Element url is note matched with expected url"

        status_code = get_status_code(element_url)
        assert status_code == 200, "Url have bad response"

        work_driver.click(data['selector'])
        url = work_driver.check_page_url(element_url)
        assert url, "Click on element dont open expected page"

    @allure.title("Static links")
    @pytest.mark.mobile
    @pytest.mark.desktop
    @pytest.mark.parametrize('name, data', test_data['static'].items())
    def test_static_links(self, work_driver, get_status_code, name, data):
        """Test:
        1) Element is clickable
        2) Link in element match to expect link
        3) Link request is valid
        4) Click on the element open link"""

        work_driver.to_main_page()

        element = work_driver.element_is_clickable(data['selector'])
        assert not isinstance(element, Exception), "Element not available"

        element_url = work_driver.get_element_url(data['selector'])
        assert element_url == ''.join([base_url, data['href']]), "Element url is note matched with expected url"

        status_code = get_status_code(element_url)
        assert status_code == 200, "Url have bad response"

        work_driver.click(data['selector'])
        url = work_driver.check_page_url(element_url)
        assert url, "Click on element dont open expected page"

    @allure.title("Form links")
    @pytest.mark.mobile
    @pytest.mark.desktop
    @pytest.mark.parametrize('name, data', test_data['forms'].items())
    def test_form_links(self, work_driver, name, data):
        """Test:
        1) Element is clickable
        2) Link in element match to expect link
        3) Click on the element open link
        4) Position after click match position of linked element"""

        work_driver.to_main_page()

        element = work_driver.element_is_clickable(data['selector'])
        assert not isinstance(element, Exception), "Element not available"

        element_url = work_driver.get_element_url(data['selector'])
        assert element_url == ''.join([base_url, data['href']]), "Element url is note matched with expected url"

        work_driver.click(data['selector'])
        url = work_driver.check_page_url(element_url)
        assert url, "Click on element dont open expected page"

        element_offset = work_driver.get_location(data['selector'])
        click_offset = work_driver.get_location()
        assert element_offset == click_offset, "Position after click not match element position"

    @allure.title("Partners links")
    @pytest.mark.mobile
    @pytest.mark.desktop
    @pytest.mark.parametrize('name, data', test_data['partners'].items())
    def test_partners_links(self, work_driver, name, data):
        """Test:
        1) Element is clickable
        2) Link in element match to expect link
        3) By click open new tab, where url match element link"""

        work_driver.to_main_page()

        element = work_driver.element_is_clickable(data['selector'])
        assert not isinstance(element, Exception), "Element not available"

        element_url = work_driver.get_element_url(data['selector'])
        assert element_url == data['href'], "Element url is note matched with expected url"

        work_driver.click(data['selector'])
        work_driver.next_tab()
        url = work_driver.check_page_url(element_url)
        work_driver.close_current_tab()
        assert url, "Click on element dont open expected page"

    @allure.title("Phone links")
    @pytest.mark.mobile
    @pytest.mark.desktop
    @pytest.mark.parametrize('name, data', test_data['tel'].items())
    def test_tel_links(self, work_driver, name, data):
        """Test:
        1) Element is clickable
        2) Link in element match to expect link"""

        work_driver.to_main_page()

        element = work_driver.element_is_clickable(data['selector'])
        assert not isinstance(element, Exception), "Element not available"

        element_url = work_driver.get_element_url(data['selector'])
        assert element_url == data['href'], "Element url is note matched with expected url"

    @allure.title("Mail links")
    @pytest.mark.mobile
    @pytest.mark.desktop
    @pytest.mark.parametrize('name, data', test_data['mailto'].items())
    def test_mail_links(self, work_driver, name, data):
        """Test:
        1) Element is clickable
        2) Link in element match to expect link"""

        work_driver.to_main_page()

        element = work_driver.element_is_clickable(data['selector'])
        assert not isinstance(element, Exception), "Element not available"

        element_url = work_driver.get_element_url(data['selector'])
        assert element_url == data['href'], "Element url is note matched with expected url"

    @allure.title("Telegram links")
    @pytest.mark.mobile
    @pytest.mark.desktop
    @pytest.mark.parametrize('name, data', test_data['telegram'].items())
    def test_telegram_links(self, work_driver, name, data):
        work_driver.to_main_page()

        element = work_driver.element_is_clickable(data['selector'])
        assert not isinstance(element, Exception), "Element not available"

        element_url = work_driver.get_element_url(data['selector'])
        assert element_url == data['href'], "Element url is note matched with expected url"

        work_driver.click_svg(data['selector'])
        work_driver.next_tab()
        url = work_driver.check_page_url(element_url)
        work_driver.close_current_tab()
        assert url, "Click on element dont open expected page"

    @allure.title("VK links mobile")
    @pytest.mark.mobile
    @pytest.mark.parametrize('name, data', test_data['vk'].items())
    def test_vk_links_m(self, work_driver, name, data):
        """Test:
        1) Element is clickable
        2) Link in element match to expect link
        3) By click open new tab, where url match element link"""

        work_driver.to_main_page()

        element = work_driver.element_is_clickable(data['selector'])
        assert not isinstance(element, Exception), "Element not available"

        element_url = work_driver.get_element_url(data['selector'])
        assert element_url == data['href'], "Element url is note matched with expected url"

        page_url = '//m.'.join(data['href'].split('//'))

        work_driver.click_svg(data['selector'])
        work_driver.next_tab()
        url = work_driver.check_page_url(page_url)
        work_driver.close_current_tab()
        assert url, "Click on element dont open expected page"

    @allure.title("VK links")
    @pytest.mark.desktop
    @pytest.mark.parametrize('name, data', test_data['vk'].items())
    def test_vk_links(self, work_driver, name, data):
        """Test:
        1) Element is clickable
        2) Link in element match to expect link
        3) By click open new tab, where url match element link"""

        work_driver.to_main_page()

        element = work_driver.element_is_clickable(data['selector'])
        assert not isinstance(element, Exception), "Element not available"

        element_url = work_driver.get_element_url(data['selector'])
        assert element_url == data['href'], "Element url is note matched with expected url"

        work_driver.click_svg(data['selector'])
        work_driver.next_tab()
        url = work_driver.check_page_url(element_url)
        work_driver.close_current_tab()
        assert url, "Click on element dont open expected page"

    @allure.title("Youtube links")
    @pytest.mark.desktop
    @pytest.mark.parametrize('name, data', test_data['youtube'].items())
    def test_youtube_links(self, work_driver, name, data):
        """Test:
        1) Element is clickable
        2) Link in element match to expect link
        3) By click open new tab, where url match element link"""

        work_driver.to_main_page()

        element = work_driver.element_is_clickable(data['selector'])
        assert not isinstance(element, Exception), "Element not available"

        element_url = work_driver.get_element_url(data['selector'])
        assert element_url == data['href'], "Element url is note matched with expected url"

        work_driver.click_svg(data['selector'])
        work_driver.next_tab()
        url = work_driver.check_page_url(element_url)
        work_driver.close_current_tab()
        assert url, "Click on element dont open expected page"

    @allure.title("Youtube links mobile")
    @pytest.mark.mobile
    @pytest.mark.parametrize('name, data', test_data['youtube'].items())
    def test_youtube_links_m(self, work_driver, name, data):
        """Test:
        1) Element is clickable
        2) Link in element match to expect link
        3) By click open new tab, where url match element link"""

        work_driver.to_main_page()

        element = work_driver.element_is_clickable(data['selector'])
        assert not isinstance(element, Exception), "Element not available"

        element_url = work_driver.get_element_url(data['selector'])
        assert element_url == data['href'], "Element url is note matched with expected url"

        page_url = 'm'.join(data['href'].split('www'))

        work_driver.click_svg(data['selector'])
        work_driver.next_tab()
        url = work_driver.check_page_url(page_url)
        work_driver.close_current_tab()
        assert url, "Click on element dont open expected page"


