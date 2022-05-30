# Import important libraries
import requests as re
from bs4 import BeautifulSoup
import lxml as xml
from itertools import zip_longest
import csv


result = re.get('https://wuzzuf.net/search/jobs/?q=python&a=hpb')
print(result)


src = result.content
print(src)


soup = BeautifulSoup(src, "lxml")
