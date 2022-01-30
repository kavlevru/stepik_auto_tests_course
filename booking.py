import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.implicitly_wait(5)

try: 
    browser.get(link)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    bookBtn = browser.find_element_by_id("book")
    bookBtn.click()
    
    submitBtn = browser.find_element_by_css_selector('[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView({block:'center'});", submitBtn)
    
    x = int(browser.find_element_by_id("input_value").text)
    x = str(math.log(math.fabs(12*math.sin(x))))
   
    input = browser.find_element_by_id("answer")
    input.send_keys(x)
    
    submitBtn.click()

finally:
    time.sleep(20)
    browser.quit()
    
