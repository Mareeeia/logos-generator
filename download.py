import json
import requests
import re
import csv
import pandas
import urllib.request

def download_image(url, name):
    fullname = "logos/" + name+".jpg"
    try:
      urllib.request.urlretrieve(url,fullname)
    except:
      pass

  
colnames = ['number', 'name', 'logo_link']
data = pandas.read_csv('bands.csv', names=colnames)
names = data['name']
links = data['logo_link']
ids = data["number"]

for i in range(0,len(links)-2):
   if (names[i] == names[i+1]):
     download_image(links[i], names[i] + str(ids[i]))
  



