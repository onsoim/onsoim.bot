
import json


class x3F:
    def __init__(self):
        self.dName      = 'data/0x3F.json'

        Jx3F            = self.get_json()
        url             = Jx3F['url']

        from REQUESTS import REQUESTS
        requests = REQUESTS()

        res = requests.get(f'{url}/airing')
        if res: 
            from bs4 import BeautifulSoup
            a = BeautifulSoup(
                res.text,
                'html.parser'
            ).select('a')
            lists = [[ s.text.strip() for s in _.select('strong') ] for _ in a if len(_.select('strong')) > 1 ]

            for list in lists: print(list)

    def get_json(self):
        with open(self.dName) as f:
            return json.load(f)


if __name__ == "__main__":
    x3f = x3F()
