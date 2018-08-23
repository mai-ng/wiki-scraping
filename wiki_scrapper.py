#####################
### Scrap data from a Wiki page, 
### Extract a list of states, years of capitals, former capitals
### Write data to a csv file
#####################

import urllib2
from bs4 import BeautifulSoup
import pandas as pd

# specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

# query the website and return the HTML
page = urllib2.urlopen(wiki)

# parse the HTML in 'page' variable, and store it in Beautifulsoup
soup = BeautifulSoup(page, "html.parser")

# get the wikitable by class
table_info = soup.find('table', class_='wikitable sortable plainrowheaders')
# print(table_info)

# Generate lists
A = []
B = []
C = []
D = []
E = []
F = []
G = []

for row in table_info.findAll('tr'):
    cells = row.findAll('td')
    states = row.findAll('th')
    if len(cells) == 6: # Extract table body, not heading
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))

df = pd.DataFrame(A, columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
print(df)

# Write data to a csv file
df.to_csv('wiki_india.csv', encoding='utf-8', index=False)
pd.read_csv('foo.csv')
