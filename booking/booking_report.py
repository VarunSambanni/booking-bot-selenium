#Includes the methods that will parse the specific data that we need from each one of the deal boxes
import collections
from selenium.webdriver.remote.webelement import WebElement

class BookingReport:

    def __init__(self, boxes_selection_element:WebElement): 
        self.boxes_selection_element = boxes_selection_element 
        self.deal_boxes = self.pull_deal_boxes()
    
    def pull_deal_boxes(self):
        return self.boxes_selection_element.find_elements_by_css_selector('div[data-testid="property-card"]')

    def pull_deal_box_attributes(self):
        collection = []
        for deal_box in self.deal_boxes: 
            hotel_name = deal_box.find_element_by_css_selector('div[data-testid="title"]').get_attribute('innerHTML').strip()
            hotel_price = deal_box.find_element_by_class_name('bd73d13072').get_attribute('innerHTML').strip() 
            hotel_score = deal_box.find_element_by_class_name('d10a6220b4').get_attribute('innerHTML').strip() 
            collection.append([hotel_name, hotel_price, hotel_score])
        return collection
