from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

URL = "https://www.binance.com/en/trade/BTC_BUSD"

# Opciones webdriver
# --------------------------------------------------------------------------------------------------------------------------------#
options = Options()
options.add_argument("--headless") # En caso se quiera trabajar con la ventana del driver abierta, comentar esta linea
options.add_argument("log-level=3")
options.add_argument('window-size=1920x1080')
driver = Chrome(executable_path='C:/WebDriver/bin/chromedriver.exe', options=options)
# --------------------------------------------------------------------------------------------------------------------------------#

wait = WebDriverWait(driver, 5)
driver.get(URL)

priceRange = []


for i in range(10):
    price = driver.find_element_by_class_name('showPrice')
    priceRange.append(price.text.replace(',', ''))
    time.sleep(2)

df = pd.DataFrame(priceRange)
df.columns = ['Price (BUSD)']

writer = pd.ExcelWriter('./Bitcoin.xlsx', engine = 'xlsxwriter')
df.to_excel(writer, sheet_name = 'BTC', index=False)
writer.save()