import urllib.request
from bs4 import BeautifulSoup as Soup
from datetime import date, timedelta
# ----------------------------------------------------------
image_number = 1
url_var = (date.today())


def download_jpg(url, file_path, doc_name):
    full_path = file_path + str(doc_name) + '.jpg'
    urllib.request.urlretrieve(url, full_path)


while image_number <= 5:
    my_url = 'https://apod.nasa.gov/apod/ap' + url_var.strftime("%y%m%d") + '.html'
    uClient = urllib.request.urlopen(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = Soup(page_html, "html.parser")
    images = page_soup.find('img')['src']
    if images[:1] == 'i':
        url_image = "https://apod.nasa.gov/apod/" + images
    else:
        url_image = images
    download_jpg(url_image, 'static/', image_number)
    image_number += 1
    url_var = url_var - timedelta(1)
