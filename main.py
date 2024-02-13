from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")

title = driver.title

driver.implicitly_wait(0.5)

inputTextName= driver.find_element(by=By.ID, value="userName")
inputTextEmail = driver.find_element(by=By.ID, value="userEmail")
inputTextAddress = driver.find_element(by=By.ID, value="currentAddress")
inputTextPermanentAddress = driver.find_element(by=By.ID, value="permanentAddress")
submitButton = driver.find_element(by=By.ID, value="submit")


inputTextName.send_keys("Ejemplo")
inputTextEmail.send_keys("a@a.com")
inputTextAddress.send_keys("cra 9 mno 78788")
inputTextPermanentAddress.send_keys("no aplica")

submitButton.click()

mensajeValidar = driver.find_element(by=By.XPATH, value="//p[@id='name']")

var = inputTextName.text in mensajeValidar.text

if var==True:
    driver.quit()