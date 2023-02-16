import allure
import pytest
from helpers.tests_data import TestData


@allure.epic("Form")
@allure.story("Field validation")
class TestForm:

    test_naming = "field_tests"
    test_data = TestData().get_sections(test_naming)

    @allure.title("Name field validation")
    @pytest.mark.desktop
    @pytest.mark.mobile
    @pytest.mark.parametrize("value, isvalid", test_data["name"].items())
    def test_name_validation(self, work_driver, value, isvalid):
        """
        Test
        1) Element is visible
        2) Fill valid/invalid text
        """
        work_driver.to_main_page()
        selector = self.test_data['selector']['name']

        element = work_driver.element_is_visible(selector)
        assert not isinstance(element, Exception), "Field is not visible"

        element.send_keys(value)

        work_driver.click(self.test_data['selector']['send'])
        classes = element.get_attribute('class')

        if isvalid is True:
            assert "form__input_error" not in classes
        else:
            assert "form__input_error" in classes

    @allure.title("Phone field validation")
    @pytest.mark.desktop
    @pytest.mark.mobile
    @pytest.mark.parametrize("value, expect", test_data["phone"].items())
    def test_phone_validation(self, work_driver, value, expect):
        """
        Test
        1) Element is visible
        2) Fill valid/invalid text
        """

        work_driver.to_main_page()
        selector = self.test_data['selector']['phone']

        element = work_driver.element_is_visible(selector)
        assert not isinstance(element, Exception), "Field is not visible"

        element.send_keys(value)

        work_driver.click(self.test_data['selector']['send'])
        classes = element.get_attribute('class')

        if expect:
            assert "form__input_error" not in classes
        else:
            assert "form__input_error" in classes

    @allure.title("Mail field validation")
    @pytest.mark.desktop
    @pytest.mark.mobile
    @pytest.mark.parametrize("value, expect", test_data["mail"].items())
    def test_mail_validation(self, work_driver, value, expect):
        """
        Test
        1) Element is visible
        2) Fill valid/invalid text
        """

        work_driver.to_main_page()
        selector = self.test_data['selector']['mail']

        element = work_driver.element_is_visible(selector)
        assert not isinstance(element, Exception), "Field is not visible"

        element.send_keys(value)

        work_driver.click(self.test_data['selector']['send'])
        classes = element.get_attribute('class')

        if expect:
            assert "form__input_error" not in classes
        else:
            assert "form__input_error" in classes


@allure.epic("Form")
@allure.story("Form response")
class TestFormRequest:

    test_naming = "form_response"
    test_data = TestData().get_sections(test_naming)

    @allure.title("Form response")
    @pytest.mark.desktop
    @pytest.mark.mobile
    @pytest.mark.parametrize("name, values", test_data["test_data"].items())
    def test_form_send(self, work_driver, name, values):
        """
        Test
        1) Element is visible
        2) Fill valid/invalid text
        """

        work_driver.to_main_page()

        send_selector = self.test_data['selector']['send']
        form_selector = self.test_data['selector']['success']
        refresh_selector = self.test_data['selector']['refresh']
        valid = values['valid']

        selector = self.test_data['selector']['name']
        element = work_driver.element_is_visible(selector)
        element.send_keys(values['name'])

        selector = self.test_data['selector']['phone']
        element = work_driver.element_is_visible(selector)
        element.send_keys(values['phone'])

        selector = self.test_data['selector']['company']
        element = work_driver.element_is_visible(selector)
        element.send_keys(values['company'])

        selector = self.test_data['selector']['mail']
        element = work_driver.element_is_visible(selector)
        element.send_keys(values['mail'])

        selector = self.test_data['selector']['comment']
        element = work_driver.element_is_visible(selector)
        element.send_keys(values['comment'])

        work_driver.click(send_selector)

        response_form_check = work_driver.check_element(form_selector)
        assert response_form_check == valid

        if valid is True:
            refresh_btn_clickble = work_driver.element_is_clickable(refresh_selector)
            assert refresh_btn_clickble

            work_driver.click(refresh_selector)
