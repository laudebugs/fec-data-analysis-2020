import json
import requests
from collections import defaultdict

# import libraries for web scraping
from bs4 import BeautifulSoup
import lxml

bidenOutputFile = open("BidenOutput.json", "r")
trumpOutputFile = open("TrumpOutput.json", "r")

bidenOutput = json.loads(bidenOutputFile.readlines()[0])
trumpOutput = json.loads(trumpOutputFile.readlines()[0])

APIcredentials = json.load(open("credentials.json","r"))
companies = defaultdict(list)

industryOutputFile = open("industries.json","r")
companies = json.load(industryOutputFile)
industryOutputFile = open("industries.json","w")

# Get a list of companies
api_calls = 15000
def getIndustries(dictionary, person):
    """
    docstring
    """
    global api_calls
    length = len(dictionary)
    i = 0
    modDict = list(dictionary.items())
    for i in range(30621,length):
        print(person +" : "+str(i)+"/"+str(length))
        companyName = modDict[i][0]
        if companyName not in companies:
            # Get the domain of the company from the Crunchbase api
            # domain = getDomain(companyName)
            # if domain== None:
            #     continue
            # Call the google api to get the Wikipedia link of the company
            key1 = APIcredentials['googleKnowledgeGraphSearchAPI']['key1']
            key2 = APIcredentials['googleKnowledgeGraphSearchAPI']['key1']
            wikiUrl = ""
            if(api_calls<100000):
                wikiUrl = getWikiUrl(companyName, key1)
                api_calls+=1
            else:
                wikiUrl = getWikiUrl(companyName, key2)
            if wikiUrl==None:
                continue
            # Scrape the Wikipedia page of the company for the industry of the company
            industry = getIndustryFromWikiLink(wikiUrl)
            if industry==None:
                continue
            print (industry)
            companies[companyName] = industry
            json.dump(companies, industryOutputFile, indent = 4) 
            # industryOutputFile.write(json.dumps(companies))

def getDomain(companyName):
    # Call the crunchbase api to get the domain of the company
    crunchbaseUrl = "https://crunchbase-crunchbase-v1.p.rapidapi.com/odm-organizations"
    querystring = {"name":companyName}
    headers = {
        'x-rapidapi-host': "crunchbase-crunchbase-v1.p.rapidapi.com",
        'x-rapidapi-key': APIcredentials['crunchBaseAPI']['x-rapidapi-key']
        }
    response = requests.request("GET", crunchbaseUrl, headers=headers, params=querystring)
    json_object = (json.loads(response.text))
    if len(json_object['data']['items'])==0:
        return None
    domain = (json_object)['data']['items'][0]['properties']['domain']
    return domain
    
def getWikiUrl(domain, key):
    # link to the Google Knowledge Graph API: https://developers.google.com/knowledge-graph/
    googleApiUrl = "https://kgsearch.googleapis.com/v1/entities:search"
    gQueryString = {
        'languages':'en',
        'query':domain,
        'key': key
    }
    # Make a request to the api
    gResponse = (requests.request("GET", googleApiUrl, params = gQueryString)).text
    if 'itemListElement' not in json.loads(gResponse):
        return None
    if len(json.loads(gResponse)['itemListElement'])==0:
        return None
    if ('detailedDescription' not in json.loads(gResponse)['itemListElement'][0]['result']):
        return None
    wikiUrl = json.loads(gResponse)['itemListElement'][0]['result']['detailedDescription']['url']
    return wikiUrl

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
    return industry

getIndustries(trumpOutput, "trump")
getIndustries(bidenOutput, "biden")

industryOutputFile.write(json.dumps(companies))