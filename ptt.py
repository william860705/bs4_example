from bs4 import BeautifulSoup
import requests as re
import pandas as pd

url = 'https://www.ptt.cc/bbs/NBA/index.html'
r = re.get(url) # 200 is ok
soup = BeautifulSoup(r.text, 'html.parser')
title = soup.find_all(class_ = 'title') # list of all titles
author = soup.find_all(class_ = 'author') # list of all authors
date = soup.find_all(class_ = 'date') # list of all dates
titles = []
authors = []
dates = []
# Put everything into lists
for t,a,d in zip(title, author, date):
    titles.append(t.text)
    authors.append(a.text)
    dates.append(d.text)

# TODO: Get content of next page
#
#
#

# Convert list to dictionary
dict = {
    'title':titles,
    'author':authors,
    'date':dates
}
# Convert dictionary into dataFrame
df = pd.DataFrame(dict)


print('The shape is: ', df.shape)
print(df)

# TODO: save df to csv

