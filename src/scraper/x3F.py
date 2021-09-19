
from SCRAPER import SCRAPER


class x3F(SCRAPER):
    def __init__(self):
        self.dName      = 'data/0x3F.json'

        Jx3F            = self.get_json()
        url             = Jx3F['url']
        lists           = Jx3F['lists']

        from REQUESTS import REQUESTS
        requests = REQUESTS()

        res = requests.get(f'{url}/airing')
        if res:
            from bs4 import BeautifulSoup
            a = BeautifulSoup(
                res.text,
                'html.parser'
            ).select('a')

            for p in [
                [ s.text.strip() for s in _.select('strong') ]
                    for _ in a if len(_.select('strong')) > 1 ]:
                index = p[-1][:-1]
                if index != "PV":
                    l = {
                        'S': 'On going',
                        'L': 0,
                        'U': []
                    } if not p[0] in lists else lists[p[0]]

                    index = int(index)
                    if l['L'] != index:
                        l['U'] = list(set(
                            l['U'] + [ i + 1 for i in range(l['L'], index) ]
                        ))
                        l['L'] = index
                        if len(p) == 3: l['S'] = p[1]

                        Jx3F['lists'][p[0]] = l
            self.set_json(Jx3F)


if __name__ == "__main__":
    x3f = x3F()
