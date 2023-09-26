# Requests Module
# - handles the transactions between the client and the server in a tidy manner
# - isn’t provided with the initial python installation
# - installed by running in Terminal: pip install -U requests
#     -U means to update the existing module if it is already installed

# EXAMPLE 1
# 1. Import requests module
import requests

# 2. Store desired URL in a variable
url = "http://www.webscrapingfordatascience.com/basichttp/" 

# 3. Use the get method from the requests module to perform a GET request on the URL; the result is stored in the r variable
  # - a GET request means return the contents of this URL
  # - Every time you enter a URL in a browser, a GET request is sent from that browser to the webs erver associated with the URL
r = requests.get(url)

# 4. Use the text method from the requests module to print the contents returned from the server
print(r.text)   # prints: Hello from the web!



# EXAMPLE 2
# Tracking Pet Popularity Online
# 1. Import requests module

# 2. Store URL in a variable
url = "https://en.wikipedia.org/wiki/Pet"

# 3. Use the get method to return contents of the URL
r = requests.get(url)   # print(r) prints: <Response [200]>

# 4. Convert the returned object into a string
r = r.text    # print(r) prints raw HTML of webpage

# 5. Store desired pets to count the number of times of appearances in a list
pets = ['cats', 'dogs', 'snakes', 'fish', 'bird', 'monkey', 'iguana']

# 6. Print out the number of mentions per pet from pets list
for pet in pets:
  print("{} : {} mentions".format(pet, r.count(pet)))