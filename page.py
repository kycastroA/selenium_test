from locators import MainPageLocators

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.locator = "FACULTADES"
        self.faculty = []

class MainPage(BasePage):

    def is_load(self):
        return self.locator in self.driver.page_source

    def get_faculty(self):
        faculties = self.driver.find_element(*MainPageLocators.faculties)
                
        for elem in faculties.text.split("("):
            if ")" in elem:
                self.faculty.append(elem.split(")")[0])

    #def get_careers(self):
        
            
        
    
