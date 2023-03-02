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
        title = self._get_title(responses)
        pdf = self._get_pdf_url(responses)
        # 发起请求
        binary = requests.get(url=pdf, headers=self.headers).content
        # 存储pdf
        with open(title+'.pdf', 'wb') as F:
            F.write(binary)

    def _get_title(self, html):
        bs = BeautifulSoup(html, 'lxml')
        title = bs.find(name='title').text.split('|')[1]
        return title

    def _get_pdf_url(self, html):
        bs = BeautifulSoup(html, 'lxml')
        pdf = bs.find(name='div', attrs={'id': 'article'}).find(name='iframe').get('src')
        pdf_url = pdf.split('#')[0]
        return pdf_url

sh = SciHub()
sh.download(doi='https://doi.org/10.1016/j.eswa.2020.113973')