import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)

MY_CSS_SELECTOR = r".shadow:nth-child(4) td:nth-child(1)"
SELECT_XPATH = r"/html/body/div/div[1]/div[1]/main/div/div[1]/div[4]/div[2]/div/div/div[2]/label/select"
OPTION_CSS = r"option[value=5]"
URL = r"https://archive.ics.uci.edu/dataset/45/heart+disease"

driver.get(URL)
wait = WebDriverWait(driver, 10)

try:
    accept_terms = wait.until(EC.element_to_be_clickable((By.XPATH, r"/html/body/div/div[1]/div[1]/div/div[2]/button")))
    accept_terms.click()
except:
    pass

select_element = wait.until(EC.element_to_be_clickable((By.XPATH, SELECT_XPATH)))
dropdown = Select(select_element)
dropdown.select_by_value("15")

Column_names = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, MY_CSS_SELECTOR)))

Column_names = [Cols.text for Cols in Column_names]
print(Column_names)
driver.quit()

print(os.getcwd())

df = pd.read_csv(r"Datasets/processed.cleveland.data", names=Column_names)
df.to_csv(r"CSV_datasets/Heart_failure.csv", index=False)
print(os.getcwd())
with open("Datasets/processed.va.data", "a") as f:
    va_rows = f.readlines()

with open("CSV_datasets/Heart_failure.csv", "a") as f:
    f.write("".join(va_rows))







