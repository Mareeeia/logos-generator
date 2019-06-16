import json
import requests
import re

def get_url(page, bands_per_page):
  start = page * bands_per_page
  return "https://www.metal-archives.com/browse/ajax-genre/g/black/json/1?sEcho=3&iColumns=4&sColumns=&iDisplayStart=" + str(start) + "&iDisplayLength=" + str(bands_per_page) + "&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&iSortCol_0=0&sSortDir_0=asc&iSortingCols=1&bSortable_0=true&bSortable_1=true&bSortable_2=true&bSortable_3=false&_=1557267156942"

def get_link(id):
  if len(id) < 4:
    return ""
  return "https://www.metal-archives.com/images/" + id[0] + "/" + id[1] + "/" + id[2] + "/" + id[3] + "/" + id + "_logo.jpg"

# -------------------------------------------

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
}

total = 35000
page = 0
bands_per_page = 500
while page * bands_per_page < total:
  r = requests.get(get_url(page, bands_per_page), headers=headers)
  bandus = json.loads(r.content)
  
  for band in bandus["aaData"]:
    band_url = band[0]
    id = re.findall(r"/(\d+)'", band_url)
    band_name = re.findall(r">(\w+)<", band_url)
    if len(id) == 0 or len(band_name) == 0:
      continue
    print(','.join([id[0], band_name[0], get_link(id[0])]))

  page += 1
