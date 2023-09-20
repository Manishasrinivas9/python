import requests
from bs4 import BeautifulSoup

def extract(page):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    url=f'https://in.indeed.com/jobs?q=python+developer&l=Hyderabad%2C+Telangana&vjk={page}'
    r=requests.get(url,headers)
    return r.status_code
print(extract(0))