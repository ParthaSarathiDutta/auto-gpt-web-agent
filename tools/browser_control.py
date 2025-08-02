from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BrowserTool:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1200, 800)

    def search_and_extract(self, query: str) -> str:
        self.driver.get(f"https://www.google.com/search?q={query.replace(' ', '+')}")
        time.sleep(2)
        try:
            result = self.driver.find_element(By.CSS_SELECTOR, 'h3')
            return f"Top search result: {result.text}"
        except Exception:
            return "No results found."

    def click_link_by_text(self, link_text: str) -> str:
        try:
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT, link_text)
            element.click()
            time.sleep(2)
            return f"Clicked on link containing: {link_text}"
        except Exception as e:
            return f"Failed to click link: {str(e)}"

    def fill_form_and_submit(self, input_name: str, value: str, submit_button_text: str = None) -> str:
        try:
            input_box = self.driver.find_element(By.NAME, input_name)
            input_box.clear()
            input_box.send_keys(value)

            if submit_button_text:
                button = self.driver.find_element(By.XPATH, f"//button[contains(text(), '{submit_button_text}')]")
                button.click()
            else:
                input_box.submit()

            time.sleep(2)
            return f"Filled '{input_name}' with '{value}' and submitted."
        except Exception as e:
            return f"Form fill failed: {str(e)}"
