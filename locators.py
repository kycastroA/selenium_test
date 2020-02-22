from selenium.webdriver.common.by import By

class MainPageLocators(object):
    faculties = (By.XPATH, "//*[@id=\"accordion\"]")

    def faculty_name(self, value,language):
        lan = 1 if language.upper()=="ES" else 2
        if value != "" or value != None:
            return "//*[@id=\"heading"+value.upper()+"\"]/h4/a/strong/text()["+lan+"]"


    

"""
Estructuras XPATH

#Facultades
//*[@id="headingFADCOM"]/h4/a/strong/text()[2] Nombre Ingles
//*[@id="headingFADCOM"]/h4/a/strong/text()[1] Nombre Español

#Carreras
//*[@id="collapseFADCOM"]/div/ul[2]/li[1]/text()
//*[@id="collapseFADCOM"]/div/ul[2]/li[1]/a
//*[@id="collapseFADCOM"]/div/ul[2]/li[1]/span
"""
