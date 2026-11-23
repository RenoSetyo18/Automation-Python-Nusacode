from pages.login_pages import LoginPage
from data.data import LOGIN_DATA
from utils.config import URL_PROD
from playwright.sync_api import expect
    
def test_login_using_valid_data(page):
    login_page = LoginPage(page)
    page.goto(URL_PROD)
    login_page.click_button_login_member()
    login_page.fill_email(LOGIN_DATA["valid_user"]["email"])
    login_page.fill_password(LOGIN_DATA["valid_user"]["password"])
    login_page.click_button_login()
    login_page.click_button_ok()
    expect(login_page.validate_name()).to_have_text(LOGIN_DATA["valid_user"]["name"])
    
def test_login_using_valid_email_invalid_password(page):
    login_page = LoginPage(page)
    page.goto(URL_PROD)
    login_page.click_button_login_member()
    login_page.fill_email(LOGIN_DATA["valid_email_invalid_password"]["email"])
    login_page.fill_password(LOGIN_DATA["valid_email_invalid_password"]["password"])
    login_page.click_button_login()
    expect(login_page.error_message()).to_be_visible()