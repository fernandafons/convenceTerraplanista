import urllib.request
from bs4 import BeautifulSoup as soup
from datetime import date
# ----------------------------------------------------------
image_number = 1


def download_jpg(url_image, file_path, image_number):
    full_path = file_path + str(image_number) + '.jpg'
    urllib.request.urlretrieve(url_image, full_path)


urlvar = (date.today().strftime("%y%m%d"))

while image_number <= 5:
    my_url = 'https://apod.nasa.gov/apod/ap' + urlvar + '.html'
    uClient = urllib.request.urlopen(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    images = page_soup.find('img')
    images = images['src']

    if images[:1] == 'i':
        url_image = "https://apod.nasa.gov/apod/" + images
    else:
        url_image = images

    download_jpg(url_image, 'images/', image_number)
    image_number += 1
    urlvar = int(urlvar) - 1
    urlvar = str(urlvar)
