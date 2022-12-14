from cgitb import text
from telnetlib import EC
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        

    def test_b_success_add_employment_status(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com") # buka situs
        time.sleep(3)
        browser.find_element(By.ID, "txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.ID, "txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)

        browser.get("https://opensource-demo.orangehrmlive.com/index.php/admin/employmentStatus") # buka halaman
        browser.find_element(By.ID,"btnAdd").click() # klik tombol add
        browser.find_element(By.ID, "empStatus_name").send_keys("Outsource") # isi value
        browser.find_element(By.ID,"btnSave").click() # klik tombol save
        time.sleep(1)
        # validasi
        welcome_act = browser.find_element(By.XPATH,"//form/div[2]").text
        welcome_exp = 'Successfully Saved'
        self.assertIn(welcome_exp, welcome_act)

    def test_c_success_update_employment_status(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com") # buka situs
        time.sleep(3)
        browser.find_element(By.ID, "txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.ID, "txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)

        browser.get("https://opensource-demo.orangehrmlive.com/index.php/admin/employmentStatus") # buka halaman
        time.sleep(3)
        browser.find_element(By.XPATH, '//a[text()="Outsource"]').click()
        time.sleep(1)
        browser.find_element(By.ID, "empStatus_name").clear() # clear value
        browser.find_element(By.ID, "empStatus_name").send_keys("New Outsource") # isi value baru
        
        
        browser.find_element(By.ID,"btnSave").click() # klik tombol sign in
        time.sleep(1)
        
        # validasi
        welcome_act = browser.find_element(By.XPATH,"//form/div[2]").text
        welcome_exp = 'Successfully Saved'
        self.assertIn(welcome_exp, welcome_act)


    def tearDown(self): 
        self.browser.close() 
        

if __name__ == "__main__": 
    unittest.main()