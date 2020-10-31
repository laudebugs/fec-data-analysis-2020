# Import librarues

from bs4 import BeautifulSoup
import lxml

# Get the links to the contributions for each month
bidenSource = json.load(open("data/bidenReports.json"))
trumpSource = json.load(open("data/trumpReports.json"))

# loop through the months:

for i in range(12){
    if 'link' in bidenSource[str(i)]:
        # Get the link
        url = bidenSource[str(i)]['link']
        
}


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