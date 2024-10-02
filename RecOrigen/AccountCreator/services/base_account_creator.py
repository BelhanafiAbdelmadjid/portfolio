from services.browser_service import BowserBot
from selenium.webdriver.common.by import By

from time import sleep

from services.utils import generate_password


class BaseCreator(BowserBot):
    def __init__(self, proton, RandomAgent=True,**kwargs) -> None:
        super().__init__(proton, RandomAgent,**kwargs)
        self.email = proton.get("email")
        self.password = proton.get("password")


    def email_verification(self,sender_kw,subject_kws,by,by_value,attribute):
        link = self.proton.get_account_verification_link(
            sender_kw=sender_kw,
            subject_kws=subject_kws,
            by=by,
            by_value=by_value,
            attribute=attribute,
        )
        print(link)
        self.navigate_to(link)




