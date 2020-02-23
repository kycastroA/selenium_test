from locators import MainPageLocators
import time

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.locator = "FACULTADES"
        self.faculty = []
        self.data_complete = {}

class MainPage(BasePage):

    def is_load(self):
        return self.locator in self.driver.page_source

    def get_faculty(self):
        faculties = self.driver.find_element(*MainPageLocators.faculties)
        for elem in faculties.text.split("("):
            if ")" in elem:
                self.faculty.append(elem.split(")")[0])
        

    def get_career_by_fac(self,value):
        for fac in self.faculty:
            time.sleep(3)
            #Buscar desplegable
            coll = self.driver.find_element(*MainPageLocators.faculty_collapsable(fac))
            coll.click()
            time.sleep(5)
            #Buscar carreras
            print(fac,value)
            carr = self.driver.find_element(*MainPageLocators.faculty_careers(fac,value))
            num_carr=len(carr.text.split("\n"))/2
            time.sleep(5)
            for i in range(1,int(num_carr)+1):
                name = self.driver.find_element(*MainPageLocators.career_name(fac,value,i)).text
                code = self.driver.find_element(*MainPageLocators.career_code(fac,value,i)).text
                link = self.driver.find_element(*MainPageLocators.career_link(fac,value,i)).text
            self.data_complete[fac]={"Name":name,"code":code,"link":link}
            time.sleep(25)
        print(self.data_complete)
        
        
            
        
    
