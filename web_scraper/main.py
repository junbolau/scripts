# Simple webscraper for NZ Accredited Employer list

from urllib.request import urlopen
import re
import pandas as pd
import requests

alphabets = 'abcdefghijklmnopqrstuvwxyz'
url = 'https://www.acc.co.nz/for-business/understanding-your-cover-options/find-an-accredited-employer?title='

company_list = []
for letter in alphabets:
    page = urlopen(url + letter.upper()).read().decode("utf-8")
    #regex: insert (.*?) between two substrings to find string in the middle
    tmp = re.findall(r'<h2 class="u-h3">(.*?)</h2>',page)
    tmp = [s.replace("&amp;","&") for s in tmp]
    tmp = [s.replace("&#039;","'") for s in tmp]
    company_list += tmp

d = {'Name':company_list}

def query_input(name):
    tmp = name[name.find("(")+1:name.find(")")]
    name = name.replace(" (" + tmp + ")","")
    name = name.replace(" Limited","")
    name = name.replace(" LIMITED","")
    name = name.replace(" LTD","")
    name = name.replace(" Ltd","")
    name = name.replace(" Partnership","")
    name = name.replace(" NZ","")
    return name

clearbit_baseurl = "https://autocomplete.clearbit.com/v1/companies/suggest?query="
urls = []

for company in d['Name']:
    company = query_input(company)
    url = clearbit_baseurl + company
    response = requests.get(url).json()
    tmp = []
    if response:
        for com in response:
            tmp.append(com['domain'])
    else:
        tmp = [""]
    urls.append(tmp)
        
             
print(len(urls),len(company_list))
d["URL"] = urls
df = pd.DataFrame(d)

df.to_csv('NZ_AE_list.csv')
print("Done!")