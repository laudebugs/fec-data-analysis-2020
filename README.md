# Campaign Finance Data Analysis for the 2020 Election Cycle 🇺🇸🐎 🐘 🏃‍♀️👮‍♀️

## Background
The 2020 Election, which is one of 2020's major events in American history presents a chance for American's voices to be heard. But even before people vote, a lot of people have made up their minds on how they would vote in the election. One way voters express their opinions is through contributing money to the presidential candidates. Donations are made to committees registered by the Federal Election Commision (FEC). Each of these committees then, in turn uses the money in some way or another to support a candidate or oppose a candidate.
<br/><br/>
In the 2020 Election cycle, as in previous elections, the FEC discloses donations made to the candidates. This project aimed at looking into individual donations made to the presidential candidates from [FEC Bulk Data download](https://www.fec.gov/data/browse-data/?tab=bulk-data). The FEC defines individual donations as donations made by individuals to political committees and are included in the itemized list if the contribution’s election cycle-to-date amount is over $200 for contributions to candidate committees or the contribution’s calendar year-to-date amount is over $200 for contributions to political action committees (PACs) and party committees<sup>1</sup>. 
<br/><br/>
The data in this research examines the itemized individual contributions made to the candidate committees: [Trumps candidate committee](https://www.fec.gov/data/candidate/P80001571/): DONALD J. TRUMP FOR PRESIDENT, INC. (FEC Committee ID: C00580100) as well as [Joe Biden's candidate committee](https://www.fec.gov/data/candidate/P80000722/): BIDEN FOR PRESIDENT (FEC Committee ID: C00703975).


## Research Goals

The project aimed to determine the total sum of contributions to the candidate committees as well as the number of contributions made and obtain the following pieces of data points:
1. The average donation of each candidate
2. From what industries did each candidate receive a large share of individual donations
    1. in terms of numbers
    2. in terms of the sum of donations
3. What is the share of employed v. unemployed v retired people who donated to each candidate

## Methodology

#### The Timeline 📅
The individual donations file contains donations by individuals from the beginning of 2019 to the end of August 2020. The bulk data, at the time of the project, did not include individual donations for the month of September and October 2020.

#### Dataset Overview and Building
Each line of the dataset looks like the following
```txt
C00402669|N|M5|P|201905089149647697|15|IND|SHANKMAN, GARY|FAIRFAX|VA|220312721|SERCO INC.|SVP CHIEF FINANCIAL OFFICER|04262019|319||A995D13BAAB3A4913A9F|1329883|||4050820191647460445
```
The FEC provides a [file description](https://www.fec.gov/campaign-finance-data/contributions-individuals-file-description/) for the file. <br/>
I wrote a simple script to parse the dataset, and extracted, for each candidate committee, calculated the following:
1. Total amount and number of donations made to the candidate committee over the time period beginning from 2019 to Aug 2020
2. The average donation `total_amount/number_of_donations` towards each candidate committee

#### Extracting Employment status statistics
Each individual donation includes information on which company the individual is employed in or whether they are self-employed, unemployed or retired. The task was then to determine which industries contributed the most to each of the candidate committees.
To match a company to an industry, I considered using an API such as [Uplead](https://www.uplead.com/api?_ga=2.115832578.521656971.1603677665-1429152117.1603677665#company-api) that returns an overview of a company. However, most of the APIs required a 💰paid subscrition or an enterprise account. The free API from [Crunchbase](https://data.crunchbase.com/v3.1/reference#odm-people), which also has an enterprise version, returns a company's `domain` address. With the domain address, I then called the [Google Knowledge Graph Search API](https://developers.google.com/knowledge-graph/) that returns a JSON-LD result that contains a description and a link to the Company's Wikipedia page. 

<br/> 
💡 One thought that came to mind is that this Knowledge Graph may be how Voice assistants look things up on the internet and perhaps return a simple description of, for instance, who Kendrick Lamar is. Worth looking into sometime.
<br/>
<br/>

If a request to the Knowledge Graph Search AOI returns a link to the Wikipedia page for the company, I scraped the wikipedia page for the `Industry` of the company contained within an element (if it exists) such as:
```html
<tr>
    <th scope="row" style="padding-right: 0.5em;">
        Industry
    </th>
    <td class="category" style="line-height: 1.35em;">
        <a href="/wiki/Conglomerate_(company)" title="Conglomerate (company)">Conglomerate</a>
    </td>
</tr>
```
Storing the company, and it's industry within a file, I then moved to consolidate the reports. <br/>
For each candidate, I calculated the total sum, and number of donations from a particular company, then in turn for each industry and has a few metrics to work with and answer the question: What industries donated the most to each presidential candidate?

## Results
Preliminary results indicate that there is a very large divide between the kinds of donors that both presidential candidates got. 

<hr/>
<sup>1</sup>: Individual Contributions ([FEC](https://www.fec.gov/introduction-campaign-finance/how-to-research-public-records/individual-contributions/))