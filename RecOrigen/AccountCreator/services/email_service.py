from protonmail import ProtonMail

from typing import Any

from bs4 import BeautifulSoup

class ProtonBot(ProtonMail):
    
    def __init__(self,email,password):
        self.email = email 
        self.password = password 
        super().__init__()

    # def login(self,email,password):
    #     super().login(email,password)
        
    
    def get_account_verification_link(
            self,
            sender_kw="glassdoor",
            subject_kws="Activate your Glassdoor account now",
            by="a",
            by_value='gd-1pqjxe8 ep11te11',
            attribute="href",
            )->str:
            
        self.login(self.email,self.password)

        # Get a list of all messages
        messages = self.get_messages()

        for message in messages :
            if sender_kw in message.sender.address and subject_kws.lower() in message.subject.lower() :
                message = self.read_message(message)
                soup = BeautifulSoup(message.body,"html.parser")
                account_validation_link = soup.find(by,class_=by_value)[attribute]
                
                return account_validation_link
                
        return None


# def create_account(driver,first_name="jid",last_name="su"):
#     from services.browser_service import BowserBot
#     import random
#     bowser = BowserBot()
#     bowser.execute_scirpt("script","test1","test2","test3","test4")

#     bowser.driver.get("https://account.proton.me/mail/signup?plan=free&ref=mail_plus_intro-mailpricing-2")

#     # email_input = bowser.target_element_sync('id',"email")
#     # email_input = bowser.target_element_sync('class', 'email-input-field')
#     # email_input.send_keys(f'{last_name}.{first_name}{random.randint(1000,9999)}')

#     bowser.driver.execute_script('''

#     ''', )

    




