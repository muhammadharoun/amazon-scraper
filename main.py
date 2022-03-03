# importing libraries
from bs4 import BeautifulSoup
import requests
from csv import writer
import json
import urllib.parse
from time import sleep
#  lxml
# configurations 
config = json.load(open('config.json','r',encoding='utf-8-sig'))

# function catch all product from amazon and save in csv
def get_amazon_products(URL,File): # ,price,rate,review
    # opening our output file in append mode
    
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
    

    # Making the HTTP Request
    webpage = requests.get(URL, headers=HEADERS)
    # Creating the Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "lxml")
    try:
        cards = soup.find_all("div", attrs={"class": 's-card-container'})
        product_data = []
        for ele in cards:
            #  get title 
            title = ele.find('h2').find('a').find('span').text
            # get rate 
            try:
                rate = float(ele.find('div', attrs={"class": 'a-row a-size-small'}).text.split(' ')[0])
            except:
                rate = 0


            # get price 
            try:
                price = float(ele.find('span', attrs={"class": 'a-offscreen'}).text.replace('ريال',''))
            except:
                price = 0

            # get link    
            try:          
                link = ele.find('h2').find('a').get('href')
            except:
                link = ''


            # get review 

            try:
                review = int(ele.find('a', attrs={"class": 'a-link-normal s-underline-text s-underline-link-text s-link-style'}).find('span').text)
            except:
                review = 0


            # if             
            product_data.append(title)
            product_data.append(price)
            product_data.append(review)
            product_data.append(rate)
            product_data.append(link)
            # print('options',config['options']['min_price'],price,config['options']['max_price'])
            if (config['options']['min_price'] < price < config['options']['max_price']) and (config['options']['min_review'] < review < config['options']['max_review']) and config['options']['min_rate'] < rate:
                
                print('>>>> title')
                writer_object = writer(File)
                writer_object.writerow(product_data) 
            product_data = []
    except AttributeError:
        title_string = "NA"

    
def add_titles(File,titles):
    writer_object = writer(File)
    writer_object.writerow(titles)   
 

def run_code():
    print('''
    - select || 1 || if to catch product 
    - select || 2 || if to update data 
    ''')
    input_val = input('    # => ')
    if input_val == '1': 
        File = open('out.csv', 'a', newline='',encoding='utf-8-sig')
        add_titles(File,['title','price','review','rate','link'])
        keyword = urllib.parse.quote(config['options']['keywords'])
        for page in range(config['options']['pages']):
            get_amazon_products(f'https://www.amazon.sa/s?k={keyword}&page={page}',File)
            print(f'https://www.amazon.sa/s?k={keyword}&page={page}')
            sleep(float(config["external_options"]['sleep']))
    elif input_val == '2':
        print('come soon')
    else:
        print('plz enter valid number')

    File.close()



if __name__ == '__main__':
    run_code()




# select section 1
# 1 - get all products  
# 2 - save products in execl sheet 

#  select section 2 
# 1- read all products from execl sheet 
# 2- updata data (add to card senario)