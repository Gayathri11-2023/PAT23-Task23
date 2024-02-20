from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
class DragAndDrop:
    #  __init__ method initializes the WebDriver and the URL.
    def __init__(self, url):
        self.driver = webdriver.Chrome()     # You can use any other WebDriver of your choice
        self.url = url
    # Open_url method is to get the url and maximize the window
    def open_url(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(5)
# switch element from iframe to another
    def switch_to_iframe(self):
        iframe = self.driver.find_element(By.CLASS_NAME, "demo-frame")
        self.driver.switch_to.frame(iframe)
# Perform the drag_and drop method
    def perform_drag_and_drop(self):
        draggable_element = self.driver.find_element(By.ID, "draggable")
        droppable_element = self.driver.find_element(By.ID, "droppable")

        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable_element, droppable_element).perform()
# switch to default content
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
# close the browser by using quit method
    def close_browser(self):
        self.driver.quit()

# Usage
url = "https://jqueryui.com/droppable/"
# object created for the class DragAndDrop
obj = DragAndDrop(url)
# To call the every method by using object
try:
    obj.open_url()
    obj.switch_to_iframe()
    obj.perform_drag_and_drop()
    obj.switch_to_default_content()
    sleep(3)

finally:
    obj.close_browser()
