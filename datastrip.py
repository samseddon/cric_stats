import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

url = "https://www.espncricinfo.com/series/icc-world-test-championship-2019-2021-1195334/england-vs-australia-3rd-test-1152848/ball-by-ball-commentary"

session = HTMLSession()
r = session.get(url)
title =  r.html.find('title')
print(title[0].text)

soup = BeautifulSoup(r.html.raw_html, features='lxml')
#print(soup)

test_class_string = '<div class = "ds-text-tight-s ds-font-bold ds-flex ds-items-center ds-justify-center ds-text-center ds-w-6 ds-h-6 ds-text-typo"'
test_class_string = '<div class="ds-text-tight-s ds-font-bold ds-flex ds-items-center ds-justify-center ds-text-center ds-w-6 ds-h-6 ds-text-typo"><span>1</span></div>'
mydivs = soup.findAll(test_class_string)

for div in mydivs:
    print(div)
    if div == test_class_string:
        print(1)
#
#test_class_string = "ds-text-tight-s ds-font-bold ds-flex ds-items-center ds-justify-center ds-text-center ds-w-6 ds-h-6 ds-text-typo"
#author = response.html.xpath(test_class_string, first=True)
#print(author)

