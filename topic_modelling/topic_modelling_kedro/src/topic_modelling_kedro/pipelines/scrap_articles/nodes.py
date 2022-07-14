"""
This is a boilerplate pipeline 'scrap_articles'
generated using Kedro 0.18.1
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd



def get_fresh_bbc_news():

    url = 'https://www.bbc.com/news/world'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html5lib' )

    regions = set()
    for link in soup.find_all('a'):
        if '/news/world/' in link.get('href'):
            regions.add(link.get('href').split('/')[3])

    df = pd.DataFrame()
    for region in regions:

        links = set()
        url = f'https://www.bbc.com/news/world/{region}'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html5lib' )
        for link in soup.find_all('a',{'class':'qa-heading-link lx-stream-post__header-link'}):
            
            if 'live' not in link.get('href') and region.replace('_','-').replace('-and-','-') in link.get('href'):
                links.add('https://www.bbc.com' + link.get('href'))

        links = list(links)

        articles = {}
        for article_link in links:

            r = requests.get(article_link)
            soup = BeautifulSoup(r.text, 'html5lib' )
            
            title = soup.find('h1').text
            text = ''
            
            for txt in soup.find_all('p',{'class':'ssrcss-1q0x1qg-Paragraph eq5iqo00'}):
                text +=(txt.text)
            
            articles[title] = text


        intermediary_df = pd.DataFrame([[region]*len(links),links,list(articles.keys()),list(articles.values())]).T.dropna()
        intermediary_df.columns = ['Region','Article_link','Title','Content']
        df = pd.concat([df,intermediary_df],axis=0)
    
    return df