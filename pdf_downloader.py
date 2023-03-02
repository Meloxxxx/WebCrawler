import requests
from bs4 import BeautifulSoup

class SciHub:
    def __init__(self):
        self.root_net = 'https://sci-hub.ren/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                                      'Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57',
                        'Referer': 'https://sci-hub.ren/'}

    def download(self, doi):
        data = {'request': doi}
        responses = requests.post(data=data, url=self.root_net, headers=self.headers).text
        print(responses)

sh = SciHub()
sh.download(doi='https://doi.org/10.1016/j.eswa.2020.113973')