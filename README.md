# BZCTwitterBotSanitized 1.0
Grabs all zombies below a certain rank and price then posts them to Twitter via a Pastebin link

Created by Schleep Cuh#6841 (Gueruex)

Any ideas or suggestions are greatly appreciated

Future Features (In no particular order)
----------------------------------------------------------
1. Add statistical analysis to define a price threshold to best fit those rank ranges on a day to day basis
2. Add a feature to display the statistical best deal for the day. This zombie's link will be placed directly in the post and the post will feature the zombie so everyone can see it.
3. Find a better workaround to grabbing zombies prices and state of sale until OS API supports Polygon projects

      3a. If a better workaround is found, we can begin thinking about grabbing all 10,000 zombies instead of just the top 20%
4. Add multithreading with proxys and new headers to bring down run speed from 2000 seconds to 2000*(# of threads)^(-1) seconds
      
Finished Features      
----------------------------------------------------------
Add different price thresholds for BZCs ranked 1-100, 101-500, 501-1000, 1001-2000 -> Community voted to keep .1 Threshold, but forward compatibility added.

Actually have the zombies json in a json file instead of taking 8000 lines in main.py (Sorry I was lazy when initially making this) -> No longer lazy

INSTALLATION
----------------------------------------------------------
Clone the project using
~~~
git clone https://github.com/gueruex/BZCTwitterBotSanitized.git
~~~
Navigate to the folder and install the requirements using
~~~
pip install -r requirements.txt
~~~
If you want the bot to post to twitter then you will have to apply for a developer account
~~~
https://developer.twitter.com/en/apply-for-access
~~~
Once you have a developer account you will need to apply for elevated access to use the 1.1 endpoint (This is free and the application is automated and instant)
~~~
https://developer.twitter.com/en/portal/products/elevated
~~~
Register for a pastebin account if you haven't already
~~~
https://pastebin.com/signup
~~~
Set up authentication setting on Twitter developer using the OAuth 1.0a option
~~~
Callback can be "http://localhost:3000"
Any other options such as TOS page and Website page can be filled with anything
~~~
Place your Twitter API Key, API Secret, Access Token, and Access Secret into the field at the top of main.py
~~~
API_KEY = 'PLACE TWITTER API KEY HERE'
API_SECRET = 'PLACE TWITTER API SECRET HERE'
ACCESS_TOKEN = 'PLACE TWITTER USER KEY HERE'
ACCESS_SECRET = 'PLACE TWITTER USER SECRET HERE'
~~~
Get your Pastebin API key and place it in the designated field in main.py
~~~
PB_KEY = 'PLACE PASTEBIN API KEY HERE'

Key can be found at https://pastebin.com/doc_api
~~~
Fill in your Pastebin username and password into the designated fields (This has to do with further authentication to post on pastebin)
~~~
PB_USERNAME = 'PLACE PASTEBIN USERNAME HERE'
PB_PASSWORD = 'PLACE PASTEBIN PASSWORD HERE'
~~~
Run the script using python ./main.py

>The script takes roughly 33 minutes and 20 seconds to run. This line to a lower sleep value, but I found 1 second has protected me from being rate limited at the moment
~~~
Line 58:  sleep(1) #Pls no time me out, pls OS support polygon soon
~~~


Socials
----------------------------------------------------------
OS: https://opensea.io/Gueruex

Twitter: https://twitter.com/GueruexN

Instagram (Inactive): @gueruex.nft

OpenSea Project
----------------------------------------------------------

https://opensea.io/collection/billionairezombiesclub (By https://opensea.io/axman_j)
