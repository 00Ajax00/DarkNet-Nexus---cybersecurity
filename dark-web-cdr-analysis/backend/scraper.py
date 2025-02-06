# backend/scraper.py
import requests
from bs4 import BeautifulSoup
import socks
import socket

TOR_PROXY = "socks5h://127.0.0.1:9050"

def scrape_darkweb(url="http://somehiddenservice.onion"):
    session = requests.session()
    session.proxies = {"http": TOR_PROXY, "https": TOR_PROXY}
    
    try:
        response = session.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return {"title": soup.title.string, "content": soup.text[:500]}
    except Exception as e:
        return {"error": str(e)}
