import tweepy
from pbwrap import Pastebin
from time import sleep
from datetime import datetime
import requests
import json

def main():
    API_KEY = 'PLACE TWITTER API KEY HERE'
    API_SECRET = 'PLACE TWITTER API SECRET HERE'
    ACCESS_TOKEN = 'PLACE TWITTER USER KEY HERE'
    ACCESS_SECRET = 'PLACE TWITTER USER SECRET HERE'
    PB_KEY = 'PLACE PASTEBIN API KEY HERE'
    PB_USERNAME = 'PLACE PASTEBIN USERNAME HERE'
    PB_PASSWORD = 'PLACE PASTEBIN PASSWORD HERE'
    baseURL = 'https://opensea.io/assets/matic/0x4bca2c2ece9402b5d4dd031b49d48166c40b7957/'
    rankDatabase = None

    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET, 'http://localhost:3000')
    twitterApi = tweepy.API(auth) #Setting up Twitter api authentication

    pbApi = Pastebin(PB_KEY) # Setting up Pastebin API authentication
    pbApi.authenticate(PB_USERNAME, PB_PASSWORD)

    passHeader = {'Accept': '*/*', 'Connection': 'keep-alive',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Safari/537.36',
                  'Cache-Control': 'max-age=0', 'DNT': '1', 'Upgrade-Insecure-Requests': '1'} #Header I use for OpenSea, can generat a new one using fake_headers library

    with open('top20.json') as f:
      rankDatabase = json.load(f)
    f.close()


    with open('zombies.txt', 'w', encoding='utf-8') as f: #Open the stream to write the zombies
      for foo in range(2000): #Loop through all top 2000 zombies
        print(foo) #Just to keep track of where it is for me, Not actually necessary
        r = requests.get(baseURL+rankDatabase[foo]["ID"], headers=passHeader) #Sending the get request
        if findStatus(r): #If the zombie is actually for sale
          price = float(findPrice(r)) #Get the price
          if price<=.1: #Check if it is below the threshold
            f.writelines(baseURL+str(rankDatabase[foo]["ID"])+ " (Rank " + str(foo) + ", " + str(price) + "Eth)\n") #Write out the line
        sleep(1) #Pls no time me out, pls OS support polygon soon
    f.close() #Close that stream baby gril

    openfile = open('zombies.txt', 'r') #Set up the paste
    paste = openfile.read()

    pbLink = pbApi.create_paste(paste, 0, "Zombie Fire Sale "+ datetime.today().strftime('%Y%m%d'), '1W') #Make the paste

    openfile = open("post.txt", 'w') #Writes the post into a file, so we can get multiline posts
    openfile.write("Zombie Fire Sale "+datetime.today().strftime('%Y%m%d')+"\n#BZC #BZCARMY #NFT\n"+pbLink)
    openfile.close() #Close that stream, I promise this is the last time

    with open('post.txt', 'r') as f: #Sorry kitten, I lied
      twitterApi.update_status(f.read()) #Make twitter post
    f.close() #Actual last time

def findPrice(r): #Stupid workaround since OS API doesn't support Polygon
  firstPrice = r.text[r.text.find('Price--amount') + 13:]
  realPrice = firstPrice[firstPrice.find('Price--amount') + 29:]
  endPrice = realPrice.find('<')
  print (realPrice[:endPrice])
  return realPrice[:endPrice].replace(",","")

def findStatus(r): #Another stupid fucking workaround my god it's so ugly
  status = r.text[r.text.find('TradeStation--ask-label')+23:]
  status = status[status.find('TradeStation--ask-label')+25:]
  if status[:13] == "Current price":
    return True
  else:
    return False

main()

'''
Pastebin Expiry Parameters
N = Never
10M = 10 Minutes
1H = 1 Hour
1D = 1 Day
1W = 1 Week
2W = 2 Weeks
1M = 1 Month
6M = 6 Months
1Y = 1 Year
'''