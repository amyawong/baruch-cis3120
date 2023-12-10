# 1. Import libraries
# Import the webdriver library from selenium
from selenium import webdriver

# Import the Options libary from the chrome options
from selenium.webdriver.chrome.options import Options

# the BY keyboard tells specifies what parameter to limit to search to (e.g. ID, CLASS_NAME, etc.)
from selenium.webdriver.common.by import By

# wait and EC allows the program to wait while the webpage loads
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


# 2. Create a Chrome web driver and set the options
chrome_options = Options()

# 3. Keep the browser window open until the user closes it
chrome_options.add_experimental_option("detach", True)

# 4. Instantiate the driver
driver = webdriver.Chrome(options= chrome_options)

# 5. Set the URL
url = "https://amazon.com/"
driver.get(url)

while True:
	pass