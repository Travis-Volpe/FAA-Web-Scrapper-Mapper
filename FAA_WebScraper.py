# FAA Web Scaping Project
import csv
import requests
import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

url = 'https://tfr.faa.gov/tfr2/list.html'
html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')

type(soup)

title - soup.title
print(title)

text = soup.get_text()
