""" Tool for browser control using Selenium """
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class BrowserTool:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    def search_and_extract(self, query: str) -> str:
        self.driver.get("https://www.google.com")
        time.sleep(1)
        box = self.driver.find_element("name", "q")
        box.send_keys(query)
        box.submit()
        time.sleep(2)
        results = self.driver.find_elements("css selector", "h3")
        top_result = results[0].text if results else "No results"
        return f"Top search result: {top_result}"

    def close(self):
        self.driver.quit()
