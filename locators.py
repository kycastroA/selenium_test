from selenium.webdriver.common.by import By

class MainPageLocators(object):
    faculties = (By.XPATH, "//*[@id=\"accordion\"]")

    def faculty_name(self, value,language):
        lan = 1 if language.upper()=="ES" else 2
        if value != "" or value != None:
            return (By.XPATH,"//*[@id=\"heading"+value.upper()+"\"]/h4/a/strong/text()["+lan+"]")

    @staticmethod
    def faculty_collapsable(value):
        if value != "" or value != None:
             return (By.XPATH,"//*[@id=\"heading"+value.upper()+"\"]/h4/a/strong")

    def faculty_careers(value,language):
        lan = 1 if language.upper()=="ES" else 2
        if value != "" or value != None:
            return (By.XPATH,"//*[@id=\"collapse"+value.upper()+"\"]/div/ul["+str(lan)+"]")

    def career_name(value,language,posicion):
        lan = 1 if language.upper()=="ES" else 2
        if value != "" or value != None:
            return (By.XPATH,f"//*[@id=\"collapse{value.upper()}\"]/div/ul[{str(lan)}]/li[str(posicion)]/text()")
            #return (By.XPATH,"//*[@id=\"collapse"+value.upper()"\"]/div/ul["+str(lan)+"]/li["+str(posicion)+"]/text()")
        
    def career_code(value,language,posicion):
        lan = 1 if language.upper()=="ES" else 2
        if value != "" or value != None:
            return (By.XPATH,"//*[@id=\"collapse"+value.upper()+"\"]/div/ul["+str(lan)+"]/li["+str(posicion)+"]/a")
        
    def career_link(value,language,posicion):
        lan = 1 if language.upper()=="ES" else 2
        if value != "" or value != None:
            return (By.XPATH,"//*[@id=\"collapse"+value.upper()+"\"]/div/ul["+str(lan)+"]/li["+str(posicion)+"]/span")
        
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
