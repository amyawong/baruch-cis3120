# webbrowser
# - a standard module thatcomes built in in Python (no need to install it via "pip")
# - used to open a browser to a specific page
# - does NOT work in Jupyter Notebooks or cloud based platforms such as Google Collaborate
# - .open_new() and .open_new_tab() are usually ignored by present-day web browsers and the URL is usually opened in a new tab

# EXAMPLE 1
# .open(url)
# - opens default web browser to specified url
import webbrowser
webbrowser.open('https://www.baruch.cuny.edu/')



# EXAMPLE 2
# .open_new(url)
# - opens url in a new window of the default browser if possible; otherwise opens url in the only browser window
webbrowser.open_new('https://www.nike.com/')



# EXAMPLE 3
# .open_new_tab(url)
# - opens url in a new tab of the default browser if possible; otherwise equivalent to open_new()
webbrowser.open_new_tab('https://www.yahoo.com/')



# EXAMPLE 4
# Build a basic Google Maps search tool by:
# - getting input from the user
# - utilizing webbrowser's open method to query google's search engine
# - open a browser to show the search results
google = input('Enter a value to search via Google Maps: ')
webbrowser.open_new_tab('https://www.google.com/maps?btnG=1&q=%s' % google)



# EXAMPLE 5
# Search for multiple items simultaneously by:
# - Storing the search terms in a list
# - Iterating through the list via a loop
# - Utilizing webbrowser's open method to query Google's search tool
# - Opening a browser to display the results - each search term will appear in a different tab
to_search = ["Brooklyn College", "Baruch College", "Hunter College", "Pizza", "Barclays Center"]
for item in to_search:
  webbrowser.open('http://www.google.com/search?btnG=1&q=%s' % item)