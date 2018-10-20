from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
my_url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'


uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")


containers = page_soup.findAll("div", {"class": "_1UoZlX"})
# print(len(containers))

# print(soup.prettify(containers[0]))

# container=containers[0]
# print(container.img['alt'])

fileName = "product_info.csv"
f = open(fileName, 'w')

# header = "Product_name,Price,raitng\n";
# f.write(header)


for container in containers:
    product_name = container.img['alt']

    price_container = container.find_all("div", {"class": "_1vC4OE _2rQ-NK"})
    price = price_container[0].text.strip()

    rating = container.find_all("div", {"class": "hGSR34 _2beYZw"})
    product_rating = rating[0].text

    #
    # rating_count = container.find_all('div',{"class": "_38sUEc"})

    #
    #
    # review_count = container.find_all("span",{"class": "_1VpSqZ"})
    # total_review_count = review_count




    trim_price = ''.join(price.split(','))
    rm_rupee = trim_price.split("₹")
    add_price = "Rs." + rm_rupee[1]
    split_price = add_price.split("E")
    final_price = split_price[0]

    split_rating = product_rating.split(" ")
    final_rating = split_rating[0]


    # print(product_name.replace(",","|")+","+final_price+","+product_rating+","+total_rating_count+","+total_review_count+"\n")
    print("Product name :"+product_name.replace(",","|")+"\n"+"Price :"+final_price+"\n"+"product rating :"+final_rating+"\n\n")

    f.write("Product name :"+product_name.replace(",","|")+"\n"+"Price :"+final_price+"\n"+"product rating :"+final_rating+"\n\n")

f.close()

