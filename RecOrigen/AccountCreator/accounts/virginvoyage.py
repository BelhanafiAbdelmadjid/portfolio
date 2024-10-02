from services.base_account_creator import BaseCreator

class VirginVoyage(BaseCreator):

    def process(self):
        self.signup()
    
    def signup(self):
        self.navigate_to("https://www.virginvoyages.com/auth/v1/signup")

        button_regsiter = self.target_element_async('class', 'SignUp_singInViaEmailButtonWrapper__04s0O')
        if button_regsiter and not button_regsiter.is_displayed():
            button_regsiter = self.target_element_async('class', 'SignUp_singInViaEmailButtonWrapper__04s0O')
        print(button_regsiter.is_displayed())
        button_regsiter.click()
        if  button_regsiter.is_displayed():
            button_regsiter.click()


        

        name = self.target_element_async('xpath', '//input[@name="firstName"]')
        name.send_keys(f'{self.user_info.get('first_name')}')

        last_name = self.target_element_async('xpath', '//input[@name="lastName"]')
        last_name.send_keys(f'{self.user_info.get('last_name')}')

        email = self.target_element_async('xpath', '//input[@name="email"]')
        email.send_keys(f'{self.email}')

        password = self.target_element_async('xpath', '//input[@name="password"]')
        password.clear()
        password.send_keys(self.password)

        from selenium.webdriver.support.ui import Select
        month_select = self.target_element_async('xpath', '//select[@aria-label="Month"]')
        select = Select(month_select)
        select.select_by_value(self.user_info.get("birth_month"))
        
        day_select = self.target_element_async('xpath', '//select[@aria-label="Day"]')
        select = Select(day_select)
        select.select_by_value(self.user_info.get("birth_day"))

        year_select = self.target_element_async('xpath', '//select[@aria-label="Year"]')
        select = Select(year_select)
        select.select_by_value(self.user_info.get("birth_year"))

        button = self.target_element_async('class', 'SignUp_submitButton__RmYlJ')
        button.click()



        









       

        

        
