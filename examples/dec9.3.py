# full_example.py

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


# 2. Create a Chrome web driver and setting the options
chrome_options = Options()

# 3. Keep the browser window open until the user closes it
chrome_options.add_experimental_option("detach", True)

#instantiating the driver
driver = webdriver.Chrome(options= chrome_options)

# 4. Set the URL
url = "https://www.amazon.com/"
driver.get(url)

# 5. Set the keyword to be entered into the search bar
keywords = ["wireless headphones", "usb drive", "usb-c charger"]

# 6. Create lists to store data
asin_list = []
product_name_list = []
product_price_list = []
product_ratings_list = []
product_ratings_num_list = []
link_list = []

# 7. Loop through list of keywords
for keyword in keywords:

    # 8. Select the search box by using its ID
    search = driver.find_element(By.ID, 'twotabsearchtextbox')  # error being thrown from this line

    # 9. Use send keys to enter text into the form field using .sendkeys()
    search.send_keys(keyword)

    # 10. Select the search button by using its ID
    search_button = driver.find_element(By.ID, 'nav-search-submit-button')

    # 11. Click the search button by using .click()
    search_button.click()

    # 12. Set wait to 5 seconds for the page to load
    driver.implicitly_wait(5)

    # 13. Collect a list of the all divs which contain the search results
    scraped_items = wait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "s-result-item s-asin")]')))


    #14. Iterate through the list of divs to find specifics of each item in the search result
    for item in scraped_items:

        # 15. Find ASIN number
        asin = item.get_attribute("data-asin")

        # 16. Find name
        # an XPATH helps you identify a specific element on a page
        product_name = item.find_element(By.XPATH, './/span[@class="a-size-medium a-color-base a-text-normal"]')


        # 17. Find price
        whole_price_list = item.find_elements(By.XPATH, './/span[@class="a-price-whole"]')
        fraction_price_list = item.find_elements(By.XPATH, './/span[@class="a-price-fraction"]')

        # 18a. If whole_price_list and fraction_price_list are NOT empty, join the dollar and cent values int one amount
        if whole_price_list != [] and fraction_price_list != []:
            product_price = '.'.join([whole_price_list[0].text, fraction_price_list[0].text])
        # 18b. Otherwise, set the price as 0
        else:
            product_price = 0

        # 19. Find ratings box
        ratings_box_list = item.find_elements(By.XPATH, './/div[@class="a-row a-size-small"]/span')

        # 20. Find ratings and ratings_num
        # 20a. If ratings_box_list is NOT empty, set the value of product_ratings and product_ratings_num
        if ratings_box_list != []:
            product_ratings = ratings_box_list[0].get_attribute('aria-label')
            product_ratings_num = ratings_box_list[1].get_attribute('aria-label')
        # 20b. Otherwise, set both values of product_ratings and product_ratings_num as 0
        else:
            product_ratings, product_ratings_num = 0, 0

        # 21. Find links of items
        link = item.find_element(By.XPATH, './/a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]').get_attribute("href")

        # 22. Append scraped information to respective lists
        asin_list.append(asin)
        product_name_list.append(product_name.text)
        product_price_list.append(product_price)
        product_ratings_list.append(product_ratings)
        product_ratings_num_list.append(product_ratings_num)
        link_list.append(link)

        print(product_name.text)
        print(product_price)
        print(product_ratings)
        print(product_ratings_num)
        print(link)
        print('\n')

    # 23. Clear the search field by using .clear() so that the next keyword in keywords list can be entered
    driver.find_element(By.ID, 'twotabsearchtextbox').clear()

    # 24. Wait 5 seconds to search again 
    time.sleep(5)
    
    # 25. Wait 5 seconds for the page to load
    driver.implicitly_wait(5)

    # 26. Remove the comment on the following line to close the browser after script completion
    # driver.quit()

# 27. Create a dictionary to store the data
df = pd.DataFrame({
  'Asin': asin_list,
  'Product Name': product_name_list,
  'Product Rating': product_ratings_list,
  'Num Ratings': product_ratings_num_list,
  'Link': link_list
})

# 28. Print the contents of the dataframe
print(df)

# 29. Export the data to a .csv file
df.to_csv('products.csv', index=False)

# 30. Close the browser
driver.quit()
