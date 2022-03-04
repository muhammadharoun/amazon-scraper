# importing libraries
from bs4 import BeautifulSoup
import requests
from csv import writer
import json
import urllib.parse
from time import sleep
#  lxml
# configurations 


def add_titles(File,titles):
    writer_object = writer(File)
    writer_object.writerow(titles)   
 
# function catch all product from amazon and save in csv
def get_amazon_products(URL,File,min_price,max_price,min_rate,min_review,max_review): # ,
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



            if ( min_price < price < max_price ) and ( min_review < review < max_review) and min_rate < rate:
                
                print('>>>> title')
                writer_object = writer(File)
                writer_object.writerow(product_data) 
            product_data = []
    except AttributeError:
        title_string = "NA"



def getConfigData(option):
    config = json.load(open('config.json','r',encoding='utf-8-sig'))

    if option == 'options': 
        return config['options']['min_price'] , config['options']['max_price'] , config['options']['min_review'] , config['options']['max_review'] , config['options']['min_rate'] , config['options']['keywords'] 
    elif option == 'external_options': 
        return config["external_options"]['file_name'] , config["external_options"]['sleep'] , config['options']['pages']
def updata_stock(URL):
    print(URL)


def run_code():
    min_price,max_price , min_review, max_review, min_rate, keywords = getConfigData('options')
    file_name, sleep_time, pages = getConfigData('external_options')

    print('''
    - select || 1 || if to catch product 
    - select || 2 || if to update data 
    ''')
    input_val = input('    # => ')
    if input_val == '1': 

        File = open(f'{file_name}.csv', 'a', newline='',encoding='utf-8-sig')
        add_titles(File,['title','price','review','rate','link'])
        keyword = urllib.parse.quote(keywords)
        for page in range(pages):
            get_amazon_products(f'https://www.amazon.sa/s?k={keyword}&page={page}',File,min_price , max_price, min_rate, min_review, max_review )
            
            sleep(float(sleep_time))
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