from services.base_account_creator import BaseCreator

class Dice(BaseCreator):

    def process(self):
        self.signup()
    
    def signup(self):
        self.navigate_to("https://www.dice.com/register/new-profile")

        for_my_self = self.target_element_async('xpath', '//button[@data-testid="first-party-button"]')
        for_my_self.click()

        first_name = self.target_element_async('xpath', '//input[@name="firstName"]')
        first_name.send_keys(self.user_info.get('first_name'))

        last_name = self.target_element_async('xpath', '//input[@name="lastName"]')
        last_name.send_keys(self.user_info.get('last_name'))
        
        email = self.target_element_async('xpath', '//input[@name="email"]')
        email.send_keys(self.email)



        #confirmPassword
        password = self.target_element_async('xpath', '//input[@name="password"]')
        password.send_keys(self.password)
        password_conf = self.target_element_async('xpath', '//input[@name="confirmPassword"]')
        password_conf.send_keys(self.password)

        
        submit_button = self.target_element_async('xpath', '//form[@name="register"]')
        submit_button.submit()


        

        
