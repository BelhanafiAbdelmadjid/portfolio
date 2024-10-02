from services.base_account_creator import BaseCreator

class Drive4southernag(BaseCreator):

    def process(self):
        self.signup()
    
    def signup(self):
        self.navigate_to("https://apply.driverreachapp.com/universal_app/_P1O9Mn0wT29gMf5GfV5_A/l/2873464/short?type=dot_app")

        first_name = self.target_element_async('xpath', '//input[@name="first_name"]')
        first_name.send_keys(self.user_info.get('first_name'))

        last_name = self.target_element_async('xpath', '//input[@name="last_name"]')
        last_name.send_keys(self.user_info.get('last_name'))


        phone_number = self.target_element_async('xpath', '//input[@name="phones-0-number"]')
        phone_number.clear()
        phone_number.click()
        from selenium.webdriver.common.keys import Keys
        # Send the DELETE key
        phone_number.send_keys(Keys.DELETE)
        phone_number.send_keys(self.user_info.get('phone_number'))
       
        email_addresses = self.target_element_async('xpath', '//input[@name="email_addresses"]')
        email_addresses.send_keys(self.email)

        submit_button = self.target_element_async('css', '.btn.btn-primary.px-5')
        submit_button.click()









       

        

        
