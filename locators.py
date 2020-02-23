from selenium.webdriver.common.by import By

class MainPageLocators(object):
    faculties = (By.XPATH, "//*[@id=\"accordion\"]")


    def faculty_name(self, value,language):
        if value != "" or value != None:
            return (By.XPATH,f"//*[@id=\"heading{value.upper()}\"]/h4/a/strong/text()[{str(language)}]")


    def faculty_collapsable(value):
        if value != "" or value != None:
             return (By.XPATH,f"//*[@id=\"heading{value.upper()}\"]/h4/a/strong")


    def faculty_careers(value,language):
        if value != "" or value != None:
            return (By.XPATH,f"//*[@id=\"collapse{value.upper()}\"]/div/ul[{str(language)}]")


    def career_name(value,language,posicion):
        if value != "" or value != None:
            return (By.XPATH,f"//*[@id=\"collapse{value.upper()}\"]/div/ul[{str(language)}]/li[{str(posicion)}]")
            
        
    def career_code(value,language,posicion):
        if value != "" or value != None:
            return (By.XPATH,f"//*[@id=\"collapse{value.upper()}\"]/div/ul[{str(language)}]/li[{str(posicion)}]/span")
        
    def career_link(value,language,posicion):
        if value != "" or value != None:
            return (By.XPATH,f"//*[@id=\"collapse{value.upper()}\"]/div/ul[{str(language)}]/li[{str(posicion)}]/a")
        
