import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/maps/place/Original+ChopShop/@33.4222924,-111.9539478,15z/data=!4m6!3m5!1s0x872b08d9682cb7e5:0xc72d69c59f87c683!8m2!3d33.422292!4d-111.9359239!16s%2Fg%2F12m91ggvh?entry=ttu&g_ep=EgoyMDI0MTAyOS4wIKXMDSoASAFQAw%3D%3D'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup.prettify())
table = soup.find('div', class_='AeaXub')