
import requests


class REQUESTS:
    def __init__(self):
        self.proxies = {
            'http': 'socks5://127.0.0.1:9050',
            'https':'socks5://127.0.0.1:9050'
        }
    
    def get(self, url):
        return requests.get(
            url,
            proxies = self.proxies
        )
