from locators.locators import locator

class LogoutPage:
    def __init__(self, page):
        self.page = page
        
    def click_button_logout(self):
        self.page.locator(locator.button_logout).click()
        
    def button_daftar(self):
        return self.page.get_by_role(locator.button_login_member[0],name=locator.button_login_member[1])