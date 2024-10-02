from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver import ChromeOptions
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .email_service import ProtonBot

class BowserBot():
    def __init__(self,proton,RandomAgent=True,**kwargs) -> None:
        self.proton = ProtonBot(email=proton.get("email"),password=proton.get("password"))
        self.driver = None
        self.user_info = kwargs

    def navigate_to(self,url):
        if not self.driver :
            self.driver = self.init_driver()
        self.driver.get(url)

    def end_driver(self):
        self.driver.quit()
        self.driver = None

    def target_element_sync(self, by, by_value, timeout=10):
        """
        Wait for an element to be present in the DOM and visible, then return it.
        
        Args:
            tag (str): The value used to locate the element (ID, class, XPath, etc.).
            by (str): The method used to locate the element ('ID', 'class', 'xpath', etc.).
            timeout (int): How long to wait for the element (default is 10 seconds).
            
        Returns:
            WebElement: The WebElement once it is found and visible.
        """
        by_method = {
            'id': By.ID,
            'class': By.CLASS_NAME,
            'xpath': By.XPATH,
            'css': By.CSS_SELECTOR,
            'name': By.NAME,
            'tag': By.TAG_NAME,
            'link_text': By.LINK_TEXT,
            'partial_link_text': By.PARTIAL_LINK_TEXT
        }

        if by.lower() not in by_method:
            raise ValueError(f"Invalid selection method '{by}'. Must be one of {list(by_method.keys())}.")

        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by_method[by.lower()], by_value))
            )
            return element
        except Exception as e:
            print(f"Error locating element: {e}")
            return None

    def target_element_async(self, by, by_value):
        """
        Wait for an element to be present in the DOM and visible, then return it.
        
        Args:
            by (str): The method used to locate the element ('ID', 'class', 'xpath', etc.).
            by_value (str): The value used to locate the element (ID, class, XPath, etc.).
            timeout (int): How long to wait for the element (default is 10 seconds).
            
        Returns:
            WebElement: The WebElement once it is found and visible.
        """
        by_method = {
            'id': By.ID,
            'class': By.CLASS_NAME,
            'xpath': By.XPATH,
            'css': By.CSS_SELECTOR,
            'name': By.NAME,
            'tag': By.TAG_NAME,
            'link_text': By.LINK_TEXT,
            'partial_link_text': By.PARTIAL_LINK_TEXT
        }

        if by.lower() not in by_method:
            raise ValueError(f"Invalid selection method '{by}'. Must be one of {list(by_method.keys())}.")

       
        element = self.driver.find_element(by_method[by.lower()], by_value)
        if element.is_displayed():
            return element

        print(f"Element with {by}='{by_value}' not found.")
        return None

    def execute_scirpt(self,script,*args):
        print(args)

    @staticmethod
    def init_driver(RandomAgent=True)->uc.Chrome:
    
        chrome_options = ChromeOptions()

        # user_profile_path = '/Users/abdelmadjidbelhanafi/Library/Application Support/Google/Chrome/'
        # chrome_options.add_argument('--user-data-dir=' + user_profile_path)

        # chrome_options.add_argument("--enable-logging")
        # chrome_options.add_argument("--log-level=0")
        # chrome_options.add_argument("--enable-performance-logging")
        # chrome_options.add_argument("--disable-webrtc")
        # chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--incognito")


        if RandomAgent : 
            ua = UserAgent()
            user_agent = ua.random
            chrome_options.add_argument(f'user-agent={user_agent}')
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        driver = uc.Chrome(options=chrome_options)
        return driver