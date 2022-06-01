"""
Web scraping is used to fetch data from an application(browser) 
just like using an API to get the desired information.

Access url/robots.txt to check all the allowed and not allowed resources from the application. 
If the website doesnt give access to their APIs then Web scraping comes into picture.

Eg - https://www.airbnb.co.in/robots.txt, https://www.moneywise.org/robots.txt, https://news.ycombinator.com/robots.txt

Useful API links - https://swapi.dev/ https://docs.github.com/en/rest

Googlebot - It is the web crawler software used by Google that collects documents from the web 
to build a searchable index for the Google Search engine (basis for all SEO)

BeautifulSoup - Python lib for web scraping (helps us to convert string to useful object for manipulation)
pprint - pprint.pprint helps with pretty print (nicely formatted output)
sorted - sorted(list,key=[lamda k:k['label'],reversed =True])

"""

from pathlib import Path
from turtle import title
import requests
from bs4 import BeautifulSoup
import pprint
import sys

def hacknews_api(page):
    res = requests.get('https://news.ycombinator.com/news?p='+str(page))
    soup = BeautifulSoup(res.text,'html.parser')
    #print(soup.text)
    # print(soup.find(id="score_31577960"))
    links = soup.select(".titlelink") # . -> accessing the class $ # -> accessing the id
    subtext = soup.select(".subtext")
    # vote = soup.select(".score")
    # print(vote[0].get('id'))
    # print(vote[0])
    return links,subtext

def sort_stories(hnlist):
    return sorted(hnlist, key=lambda k:k['points'], reverse=True) # imported sort concept - sort list of dict

def custom_news(links,subtext):
    hn =[]
    for index, item in enumerate(links): # enumerate helps with grabbing elements on the same index
        title = links[index].getText()
        #title = item.getText() # alternate way
        href = links[index].get('href',None)
        #href = item.get('href',None) # alternate way
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points>99:
                hn.append({'title':title,'href':href,'points':points})
    return sort_stories(hn)

def main(pages):
    for page in range(1,pages):
        links, subtext = hacknews_api(page)
        hn = custom_news(links,subtext)
        pprint.pprint(hn)
        print(f"End of page {page} result") 

if __name__ == '__main__':
    pages = int(sys.argv[1])
    main(pages)