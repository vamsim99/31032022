import webdriver_manager.chrome
from selenium import webdriver
from webdriver_manager.chrome  import ChromeDriverManager
import time


product = input("Enter the product name:")

print("Test case started")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.flipkart.com/")
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
driver.find_element_by_name("q").send_keys(product)
driver.find_element_by_class_name("L0Z3Pu").click()
time.sleep(5)
driver.close()
print("Test case closed")

