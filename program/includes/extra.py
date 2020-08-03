from bs4 import BeautifulSoup
from colorama import Fore as F, init

init()


def scrapper():

    """
    Scrape Html elements in this method Using BS4 & BeautifulSoup or any other tool.
    :return List, Single Variable, Tuple, Int, Dict:
    """

    pass

def banner():
    """
    Banner Which loads when the tool starts, Ascii
    For More banners Visit: http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
    :prints Ascii Banner
    """

    color = F.LIGHTBLUE_EX  # Change Color Of banner

    print(color+"""
    
     ▄▄▄▄    ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  
    ▓█████▄ ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
    ▒██▒ ▄██▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
    ▒██░█▀  ░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
    ░▓█  ▀█▓ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
    ░▒▓███▀▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
    ▒░▒   ░   ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
    
    """)


green_box = F.BLUE + '[' + F.LIGHTGREEN_EX + '+' + F.CYAN + ']'
red_box = F.BLUE + '[' + F.LIGHTRED_EX + '-' + F.CYAN + ']'
info_box = F.BLUE + '[' + F.LIGHTYELLOW_EX + '?' + F.CYAN + ']'
