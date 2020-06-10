from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
# opening the connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
page_soup.h1

# grabs each product
containers = page_soup.find_all("div", {"class":"item-container"})
filename = "products.csv"
# f = open(filename, "w")
headers = "brand, product_name, shipping\n"
# f.write(headers)
# title_container = page_soup.find_all('head', {"title"})
# for container in containers:
#     brand = containers.div.div.a.img["title"]
# brand_container = page_soup.find_all('a', {'class': 'item-brand'})
# for i in brand_container:
#     print(i.img["title"])
    # product_name = title_container[0].txt
shipping_container = containers.findAll("li", {"class": "price-ship"})
    # shipping = shipping_container[0].text.strip()
    # print("brand: " + brand)
    # print("title: " + product_name)
    # print("shipping: " + shipping_container)
# print(title_container)
# print("Brand: ", brand_container.img["title"])


# f.write("Title is {} {} {}.".format(title_container, x, y))

# f.close()