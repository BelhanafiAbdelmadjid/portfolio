from services.base_account_creator import BaseCreator

class GlassDoor(BaseCreator):
  

    def process(self):
        # self.signup()
        self.email_verification(
            sender_kw="glassdoor",
            subject_kws="Activate your Glassdoor account now",
            by="a",
            by_value='gd-1pqjxe8 ep11te11',
            attribute="href",
        )

    def signup(self):
        self.navigate_to("https://www.glassdoor.com/")

        email_input = self.target_element_async('id', 'inlineUserEmail')
        email_input.send_keys(self.email)

        login_button = self.target_element_async('css', '[data-test="email-form-button"]')
        login_button.click()
        
        email_input = self.target_element_sync('id', 'inlineUserPassword')
        email_input.send_keys(self.password)
        signup_button = self.target_element_sync('css', "button.Button[type='submit']")
        signup_button.click()


        self.driver.quit()

   




