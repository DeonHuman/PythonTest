from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import unittest
import requests

#using the chrome webdriver and navigating to the localhost address where the front end application is running on port 3000
driver = webdriver.Chrome()
driver.get("http://localhost:3000/")




# UI test 1 
print("this is UI test 1")
#waiting so that all elements are loaded on the page
time.sleep(3)

title_heading = driver.find_element(By.XPATH, '/html/body/section/main/table/thead/tr/th[1]').click()

# waiting after the click / sorting of the title column so that all elements are loaded on the page
time.sleep(3)

#checking the name of the last item in the list is equal to "The Phantom Menace"

def last_item(self): 
        firstValue = "The Phantom Menace"
        secondValue = driver.find_element(By.XPATH, '/html/body/section/main/table/tbody/tr[6]/td[1]/a').text
        # error message in case of test case failure
        message = "The last value are not equal to The Phantom Menace !"
        # assertEqual() to check if the first & second value are the same
        self.assertEqual(firstValue, secondValue, message)






# UI test 2
print("this is UI test 2")
#finding the xpath of the ... element
secondtest = driver.find_element(By.XPATH, '/html/body/section/main/table/tbody/tr[2]/td[1]/a').click()

# adding a sleep delay so that all the elements in the UI is loaded before the next step
time.sleep(3)

def wookie(self): 
        firstValue = driver.find_element(By.XPATH, '/html/body/section/main/div[2]/div[3]/ul/li[3]').text
        secondValue = driver.find_element(By.XPATH, '/html/body/section/main/div[2]/div[3]/div/h1').text
        print("secondValue")
        # error message in case test case fails 
        message = "The value of Wookie does not appear in this list !"
        # assertIn() to check equality of first & second value 
        self.assertIn(firstValue, secondValue, message)
        
        
        
                
               
        

# UI test 3
print("this is UI test 3")
# finding the xpath of the back button on the UI
back = driver.find_element(By.XPATH, '/html/body/section/nav/a').click()

# adding a sleep delay so that all the elements in the UI is loaded before the next step
time.sleep(3)

#clicking on the The Phantom Menace link from the list of movies
thirdtest = driver.find_element(By.XPATH, '/html/body/section/main/table/tbody/tr[4]/td[1]/a').click()

# adding a sleep delay so that all the elements in the UI is loaded before the next step
time.sleep(3)

def camino(self): 
        firstValue = driver.find_element(By.XPATH, '/html/body/section/main/div[2]/div[3]/ul/li[3]').text
        secondValue = driver.find_element(By.XPATH, '/html/body/section/main/div[2]/div[2]/ul').text
        print(secondValue)
        # # error message in case test case fails 
        message = "The value of camino not appear in this list !"
        # # assertNotEqual() to check equality of first & second value 
        self.assertNotEqual(firstValue, secondValue, message)







# API test 1 : get the list of movies and assert that the count of films is equal to 7, this particular api site I used returns 7
print("this is API test 1")

#doing a get request to the api link which returns all of the films
response = requests.get('https://swapi.py4e.com//api/films')
# assigning the response from the get api call to a variable to that i can assert for a value in the response, 
api_response_text = response.text

#print (api_response_text) , I was using this for troublshooting, to see the response data being returned on my api get request
# had to use an escape character \ to be able to assert for the exact text "count" : 7 , otherwise you will be running into syntax issues. I did a count of 7 as that is the number of films returned on this specific api used
expected_text = "\"count\":7"

# also adding a message here if the assert text is not present in the response value that I get from the api
assert expected_text in api_response_text, f"Text '{expected_text}' not found!"






# API test 2 : get the 3rd movie and check if the director is  ‘Richard Marquand’
print("this is API test 2")
response = requests.get('https://swapi.py4e.com//api/films/3')
api_response_text = response.text

expected_text = "\"director\":\"Richard Marquand\""  
# also adding a message here if the assert text is not present in the response value that I get from the api
assert expected_text in api_response_text, f"Text '{expected_text}' not found!"






# API test 3 : get the 5th move and assert that that the ’Producers’ are not ‘Gary Kurtz, George Lucas'
print("this is API test 3")
response = requests.get('https://swapi.py4e.com//api/films/5')
api_response_text = response.text

expected_text1 = "\"producer\": \"Gary Kurtz\""  
expected_text2 = "\"director\":\"George Lucas1\""
# also adding a message here if the assert text is not present in the response value that I get from the api
assert expected_text1 not in api_response_text, f"Text '{expected_text1}' found!"
assert expected_text1 not in api_response_text, f"Text '{expected_text2}' found!"




print("the end")

driver.quit()