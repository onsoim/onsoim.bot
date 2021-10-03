
from command.scraper.SCRAPER import SCRAPER


class x3F(SCRAPER):
    def __init__(self):
        self.dName      = 'data/0x3F.json'

        Jx3F            = self.get_json()
        url             = Jx3F['url']
        lists           = Jx3F['lists']

        from command.scraper.REQUESTS import REQUESTS
        requests = REQUESTS()

        res = requests.get(f'{url}/airing')
        if res:
            from bs4 import BeautifulSoup
            a = BeautifulSoup(
                res.text,
                'html.parser'
            ).select('a')

            from command.scraper.HANGEUL import HANGEUL

            self.new = {}
            for p in [
                [ s.text.strip() for s in _.select('strong') ]
                    for _ in a if len(_.select('strong')) > 1 ]:
                index = p[-1][:-1]
                if index != "PV":
                    name = ''.join([
                        i[0] for i in HANGEUL().seperate_jamo(p[0])
                    ])
                    l = {
                        'F': p[0],
                        'S': 'On going',
                        'L': 0,
                        'U': [],
                        'W': {}
                    } if not name in lists else lists[name]

                    index = int(index)
                    if l['L'] != index:
                        self.new[name] = [ i + 1 for i in range(l['L'], index) ]
                        l['U'] = list(set(
                            l['U'] + self.new[name]
                        ))
                        l['L'] = index
                        if len(p) == 3: l['S'] = p[1]

                        Jx3F['lists'][name] = l
            self.set_json(Jx3F)


if __name__ == "__main__":
    x3f = x3F()
