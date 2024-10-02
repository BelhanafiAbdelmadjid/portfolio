from services.base_account_creator import BaseCreator

class Fairygoodboss(BaseCreator):

    def process(self):
        self.signup()
    
    def signup(self):
        self.navigate_to("https://fairygodboss.com/")

        button_regsiter = self.target_element_async('xpath', '//button[@data-qa="main-value-props-get-started"]')
        button_regsiter.click()

        button_email = self.target_element_async('xpath', '//div[@class="call-to-action-button-text" and @data-qa="continue"]')
        button_email.click()


        email = self.target_element_async('css', '[data-qa="email"]')
        email.send_keys(self.email)

        name = self.target_element_async('xpath', '//input[@name="username-input-reset-password"]')
        name.send_keys(f'{self.user_info.get('first_name')} {self.user_info.get('last_name')}')


        password = self.target_element_async('css', '[data-qa="password"]')
        password.send_keys(self.password)

        submit_button = self.target_element_async('xpath', '//input[@name="search"]')
        submit_button.click()









       

        

        
