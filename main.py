import unittest
import page

from selenium import webdriver


path = "C:\\Users\\Karla\\Downloads\\chromedriver_win32\\chromedriver.exe"
url_page = "http://www.espol.edu.ec/es/educacion/grado/catalogo"

class ESPOL_career(unittest.TestCase):

    def setUp(self):
         self.driver = webdriver.Chrome(path)
         self.driver.get(url_page)
        

    def test_store_careers(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_load(), "Page of careers wasn't found"
        main_page.get_faculty()

        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
     unittest.main()

