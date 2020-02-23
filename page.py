from locators import MainPageLocators
import time

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.name_file = "Careers of ESPOL"
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
        lan = 1 if value.upper()=="ESPAÑOL" else 2
                
        for i,fac in enumerate(self.faculty):
            if i==0:
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight/4);")
            elif i < len(self.faculty) - 1:
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight/2);")
            else:                
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            self.data_complete.setdefault(fac,[])
            time.sleep(3)
            #Buscar desplegable
            coll = self.driver.find_element(*MainPageLocators.faculty_collapsable(fac))
            coll.click()
            time.sleep(5)
            #Buscar carreras
            carr = self.driver.find_element(*MainPageLocators.faculty_careers(fac,lan))
            num_carr=int(len(carr.text.split("\n"))/2)
            time.sleep(5)
            for i in range(1,num_carr+1):
                name = self.driver.find_element(*MainPageLocators.career_name(fac,lan,i))
                code = self.driver.find_element(*MainPageLocators.career_code(fac,lan,i))
                link = self.driver.find_element(*MainPageLocators.career_link(fac,lan,i))
                val=(name.text.split("(")[0],code.text,link.get_attribute('href'))
                self.data_complete[fac].append(val)

    def write_file(self):
        with open(self.name_file+".csv","w")as file:
            file.write(f"Name_career_en;Code_career;Faculty_name;Link_to_career_curriculum\n")

            for faculty,data_faculty in self.data_complete.items():
                for career in data_faculty:
                    file.write(f"{career[0]};{career[1]},{faculty};{career[2]}\n")
            file.close()
            
        
            
        
    
