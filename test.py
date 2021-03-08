import requests
from bs4 import BeautifulSoup
import urllib.request

page = urllib.request.urlopen('http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/')