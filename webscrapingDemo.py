from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

from bs4 import BeautifulSoup
html_doc = urlopen("http://clubelo.com/ESP")
soup = BeautifulSoup(html_doc, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))
