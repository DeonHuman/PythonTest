from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import unittest
import requests

driver = webdriver.Chrome()

driver.get("http://localhost:3000/")

# UI test 1 

time.sleep(3)

title_heading = driver.find_element(By.XPATH, '/html/body/section/main/table/thead/tr/th[1]').click()

time.sleep(3)

#checking the name of the last item in the list is equal to "The Phantom Menace"

def last_item(self): 
        firstValue = "The Phantom Menace"
        secondValue = driver.find_element(By.XPATH, '/html/body/section/main/table/tbody/tr[6]/td[1]/a').text
        # error message in case if test case got failed 
        message = "The last value are not equal to The Phantom Menace !"
        # assertEqual() to check equality of first & second value 
        self.assertEqual(firstValue, secondValue, message)

# self.last_item = driver.find_element(By.XPATH, '/html/body/section/main/table/tbody/tr[6]/td[1]/a').text
# assertEqual(self.last_item, "The Phantom Menace")

# UI test 2
#finding the xpath of the ... element
secondtest = driver.find_element(By.XPATH, '/html/body/section/main/table/tbody/tr[2]/td[1]/a').click()

# adding a sleep delay so that all the elements in the UI is loaded before the next step
time.sleep(3)

def wookie(self): 
        firstValue = driver.find_element(By.XPATH, '/html/body/section/main/div[2]/div[3]/ul/li[3]').text
        secondValue = driver.find_element(By.XPATH, '/html/body/section/main/div[2]/div[3]/div/h1').text
        print("secondValue")
        # error message in case if test case got failed 
        message = "The value of Wookie does not appear in this list !"
        # assertIn() to check equality of first & second value 
        self.assertIn(firstValue, secondValue, message)

# UI test 3
# finding the xpath of the back button on the UI
back = driver.find_element(By.XPATH, '/html/body/section/nav/a').click()

# adding a sleep delay so that all the elements in the UI is loaded before the next step
time.sleep(3)

thirdtest = driver.find_element(By.XPATH, '/html/body/section/main/table/tbody/tr[4]/td[1]/a').click()

# adding a sleep delay so that all the elements in the UI is loaded before the next step

time.sleep(3)

def wookie(self): 
        firstValue = driver.find_element(By.XPATH, '/html/body/section/main/div[2]/div[3]/ul/li[3]').text
        secondValue = driver.find_element(By.XPATH, '/html/body/section/main/div[2]/div[2]/ul').text
        # error message in case if test case got failed 
        message = "The value of Wookie does not appear in this list !"
        # assertNotEqual() to check equality of first & second value 
        self.assertNotEqual(firstValue, secondValue, message)



# API test 1 : get the list of movies and assert that the count of films is equal to 6

response = requests.get('https://swapi.py4e.com//api/films')
api_response_text = response.text

#print (api_response_text)
# had to use an escape character \ to be able to assert for the exact text "count" : 6 , otherwise you will be running into syntax issues , so by using the escape character i can assert for value "count" : 6
expected_text = "\"count\":7"
# assert expected_text in api_response_text, f"Expected text '{expected_text}' not found in API response."
#assertequal(expected_text, api_response_text, "it is present")

# also adding a message here if the assert text is not present in the response value that I get from the api
assert expected_text in api_response_text, f"Text '{expected_text}' not found!"




# API test 2 : get the 3rd movie and check if the director is  ‘Richard Marquand’

response = requests.get('https://swapi.py4e.com//api/films/3')
api_response_text = response.text

#print (api_response_text)
expected_text = "\"director\":\"Richard Marquand\""  
assert expected_text in api_response_text, f"Text '{expected_text}' not found!"




# API test 3 : get the 5th move and assert that that the ’Producers’ are not ‘Gary Kurtz, George Lucas'

response = requests.get('https://swapi.py4e.com//api/films/5')
api_response_text = response.text
print (api_response_text)

expected_text1 = "\"producer\": \"Gary Kurtz\""  
expected_text2 = "\"director\":\"George Lucas1\""
assert expected_text1 not in api_response_text, f"Text '{expected_text1}' found!"
assert expected_text1 not in api_response_text, f"Text '{expected_text2}' found!"




print("the end")

driver.quit()

