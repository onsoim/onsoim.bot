
from SCRAPER import SCRAPER


class GSS(SCRAPER):
    def __init__(self):
        self.dName      = 'data/notice.json'

        Jnotice         = self.get_json()
        url             = Jnotice['url']
        prev_notices    = Jnotice['notices']
        prev_top_notices= Jnotice['top-notices']
        last_notice_num = int(next(iter(prev_notices))) if prev_notices else 0

        from bs4 import BeautifulSoup
        from REQUESTS import REQUESTS
        requests = REQUESTS()

        trs = BeautifulSoup(
            requests.get(f'{url}?articleLimit=30').text,
            'html.parser'
        ).select('tr')[1:]

        tds = []
        for tr in trs:
            tds.append([[ td.text.strip() for td in tr.select('td') ], tr.find('a')['href']])

        top_notices, notices, new = [], {}, []
        for td in tds:
            td, href = td[0], td[1]
            notice = [ {
                'Title' : td[1],
                'Writer': td[2],
                'href': Jnotice['url'] + href
            } ]

            # Top-Notice
            if not td[0]: top_notices += notice
            # Notice
            else:
                notices[td[0]] = notice
                if int(td[0]) > last_notice_num or prev_notices[td[0]][0]['Title'] != td[1]:
                    new += notice

        Jnotice['top-notices']  = top_notices
        Jnotice['notices']      = notices
        self.set_json(Jnotice)

        self.new    = {
            'top_notices': [ x for x in top_notices if x not in prev_top_notices ],
            'notices': new
        }

    def test(self):
        msg = []

        for m in self.new['top_notices'] + self.new['notices']:
            msg.append(f"> {m['Writer']}\n> {m['Title']}\n> {m['href']}")

        print("\n\n".join(msg))


if __name__ == "__main__":
    gss = GSS()
    gss.test()
