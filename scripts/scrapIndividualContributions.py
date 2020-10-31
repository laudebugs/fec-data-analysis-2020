# Import librarues

from bs4 import BeautifulSoup
import lxml
import requests
import json

# Get the links to the contributions for each month
bidenSource = json.load(open("data/bidenReports.json"))
trumpSource = json.load(open("data/trumpReports.json"))

# loop through the months:
for year in bidenSource:
    for month in range(1,12):
        if 'link' in bidenSource[year][str(month)]:
            # Get the link
            link = bidenSource[year][str(month)]['link']
            source = requests.get(link,timeout=300).text;

            soup = BeautifulSoup(source, 'lxml');
            
            table = soup.find('tbody',class_="tablebody reportTable");

            print(table);



def getIndustryFromWikiLink(wikiUrl):
    # do some web scraping
    # Get the wikipedia page
    source = requests.get(wikiUrl).text
    soup = BeautifulSoup(source, 'lxml')
    # Look for the table that contains the info of the company
    element = soup.find("table", class_="infobox vcard")
    result = soup.find('th', text="Industry")
    if result == None:
        return None
    parent = result.parent
    if parent==None:
        return None
    if parent.td==None:
        return None
    if parent.td.a==None:
        return None
    
    industry = parent.td.a.text
    print(parent)
    return industry