from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

chromedriver = "/opt/homebrew/bin/chromedriver"
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("headless")
driver = webdriver.Chrome(options=options)


url = 'https://survey.stackoverflow.co/2022'
driver.get(url)

tableOfPopular = driver.find_element(By.XPATH, "//table[@id='languageqmfte']")


listOfPopular = tableOfPopular.find_element(By.XPATH, ".//tbody")
listOfPopular = listOfPopular.find_elements(By.XPATH, ".//tr")

data = []

for row in listOfPopular:
    curName = row.find_element(By.XPATH, ".//td").text.strip()
    curPersentage = row.find_element(By.XPATH, ".//span").text.strip()
    data.append({
        "ProgrammingLanguages": curName,
        "Hot": curPersentage
    })


tableOfPaying = driver.find_element(By.XPATH, "//table[@id='programming-scripting-and-markup-languages6z4bv']")
listOfPaying = tableOfPaying.find_element(By.XPATH, ".//tbody")
listOfPaying = listOfPaying.find_elements(By.XPATH, ".//tr")

cnt = 0

for row in listOfPaying:
    curName = row.find_element(By.XPATH, ".//td").text.strip()
    curPaying = row.find_element(By.XPATH, ".//span").text.strip()

    for key in data:
        if key["ProgrammingLanguages"] == curName:
            key["AveragePaying"] = curPaying

# Writing data to a JSON file
with open('output.json', 'w') as json_file:
    json.dump(data, json_file, indent=2)

driver.quit()



