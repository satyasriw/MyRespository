from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WD
import time
import CheckBoxFunction as Check

exec_path = r"C:\Drivers\geckodriver-v0.29.0-win64\geckodriver.exe"
URL = "https://inderpsingh.blogspot.com/2013/01/HTMLCSSQuiz1.html"
driver=webdriver.Firefox(executable_path=exec_path)
Wait_Time = 15
Wait_For = WD(driver,Wait_Time)
CheckBox_Locator= "option"
driver.get(URL)

i=0
while i <10:
    i += 1
    driver.execute_script("window.scrollBy(0,120)", "") # this will scroll the window by 120 pixel and the empty string displays the correct answer
    Element1_Check = Wait_For.until(EC.presence_of_element_located((By.NAME,CheckBox_Locator + str(i) +"1")))
    Element2_Check = Wait_For.until(EC.presence_of_element_located((By.NAME,CheckBox_Locator + str(i) +"2")))
    Element3_Check = Wait_For.until(EC.presence_of_element_located((By.NAME,CheckBox_Locator +str(i) + "3")))
    Element1_Check.click()
    Element2_Check.click()
    Element3_Check.click() # Check box 1,2,3 are selected and validating if the questions are answered correct.
    if Check.answered(driver,i): continue
    Element1_Check.click()  # check box 2 and 3 are selected as 1 has been deselected on a click
    if Check.answered(driver,i): continue
    Element1_Check.click()
    Element2_Check.click()  # check box 1 and 3 are selected as 2 has been deselected on a click
    if Check.answered(driver,i): continue
    Element2_Check.click()
    Element3_Check.click()  # Check box 1, 2 are selected as 3 has been deselected on a click
    if Check.answered(driver,i): continue
    Element2_Check.click()  # check box 1 is selected as 2 is deselected on a click
    if Check.answered(driver,i): continue
    Element1_Check.click()
    Element2_Check.click()  # check box 2 is selected
    if Check.answered(driver,i): continue
    Element2_Check.click()
    Element3_Check.click()  # check box 3 is selected






