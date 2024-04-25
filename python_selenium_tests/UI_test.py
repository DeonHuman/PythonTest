from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\temp\chromedriver_win32\chromedriver.exe')
driver.get("http://localhost:3000/")
driver.quit()