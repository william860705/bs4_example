import requests
from bs4 import BeautifulSoup
import pandas as pd

# TODO: Let user give query
google_url = "https://www.google.com/search?q=python"
response = requests.get(google_url)
soup = BeautifulSoup(response.text, "html.parser")

result_div = soup.find_all('div', attrs = {'class': 'ZINbbc'})

links = []
titles = []
descriptions = []
for r in result_div:
    # Checks if each element is present, else, raise exception
    try:
        link = r.find('a', href = True)
        title = r.find('div', attrs={'class':'vvjwJb'}).get_text()
        description = r.find('div', attrs={'class':'s3v9rd'}).get_text()
        print(title)
        # Check to make sure everything is present before appending
        if link != '' and title != '' and description != '': 
            links.append(link['href'])
            titles.append(title)
            descriptions.append(description)
    # Next loop if one element is not present
    except:
        continue

print(titles)
# TODO: 
# 1. convert list links, titles, descriptions to dictionary
# 2. convert dictionary to dataframe
# 3. save dataframe to csv