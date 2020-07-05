import requests
import urllib.request
from bs4 import BeautifulSoup

url = "https://lms.uzh.ch/dmz/"
req = requests.get(url)
#print(req.text)

#find "People"
indexPeople = req.text.index("People")
i = 0
#find "("
while req.text[indexPeople-i] != "(":
    i+=1
#print(req.text[indexPeople-i])
filter = req.text[indexPeople-i+1:indexPeople]
people = int(filter)
print(people)
