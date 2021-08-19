from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WD
from selenium.webdriver.common.by import By

WaitTime = 15

def answered(d,Question_Num): # here d is the driver and the second parameter is Question number
  WaitFor = WD(d,WaitTime)
  answer_element = WaitFor.until(EC.presence_of_element_located((By.NAME,"answer" + str(Question_Num))))
  if "Correct." in answer_element.get_attribute("value"):
    return True
  else:
    return False

