from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("http://www.cricbuzz.com/cricket-match/live-scores")
bsObj = BeautifulSoup(html.read(),  "html.parser");

complete = bsObj.findAll("a" , {"class" : "cb-lv-scrs-well-complete"})

live = bsObj.findAll("a" , {"class" : "cb-lv-scrs-well-live"})
 
for link in live:

    
    divs = link.findAll("div" , {"class" : "cb-lv-scrs-col" })
    
    for div in divs: 
        matchInfo = div.parent.parent.previousSibling
        print(matchInfo.text)
        print(div.text)
        #print(div2.text)
        

for link in complete:
    divs = link.findAll("div" , {"class" : "cb-lv-scrs-col" })
    for div in divs: 
        print(div.text)
       
