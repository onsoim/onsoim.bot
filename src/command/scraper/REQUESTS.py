
import requests


class REQUESTS:
    def __init__(self):
        self.proxies = {
            'http': 'socks5://127.0.0.1:9050',
            'https':'socks5://127.0.0.1:9050'
        }

    def get(self, URL):
        # Regular mode requests
        res = requests.get(
            URL,
            proxies = self.proxies
        )

        # Cloudflare mode requests
        cURL = "https://www.cloudflare.com"
        if res.status_code == 403 and cURL in res.text:
            import cfscrape
            res = cfscrape.create_scraper().get(
                URL
            )

        return res
