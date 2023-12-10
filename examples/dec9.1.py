# example_1.py
# via https://github.com/avinashjairam/avinashjairam.github.io/blob/master/example_1.py

# 1. Import libraries
from selenium import webdriver
import time

# 2. Create a Chrome web driver
driver = webdriver.Chrome()
# webdriver allows python to control our browser
# can configure selenium to work with any browser

# 3. Set the URL
url = "https://www.amazon.com/"
driver.get(url)

# 4. Keep the browser window open for 10 seconds
time.sleep(10)

# 5. Close the browser
driver.quit()