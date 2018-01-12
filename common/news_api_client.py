import requests


from json import loads

NEWS_API_ENDPOINT = 'https://newsapi.org/v1/'
NEWS_API_KEY = 'b908db6376e648729f7c0dd53f166c94'

ARITICLES_API = 'articles'

BBC_NEWS = 'bbc-news'
BBC_SPORT = 'bbc-sport'
CNN = 'cnn'

DEFAULT_SOURCE= [BBC_NEWS,CNN]
SORT_BY_TOP = 'top'

def buildUrl(endPoint = NEWS_API_ENDPOINT, apiName = ARITICLES_API):
    return endPoint + apiName

def getNewsFromSource(sources=DEFAULT_SOURCE, sortBy=SORT_BY_TOP):
    articles = []

    for source in sources:
        payload = {'apiKey':NEWS_API_KEY,
                    'source':source,
                    'sortBy':sortBy}
        response = requests.get(buildUrl(),params = payload)
        print response.content
        res_json = loads(response.content) # loads turn response into json

        #extract info from response
        if(res_json is not None and
            res_json['status'] =='ok' and
            res_json['source'] is not None):
            #populate news article in each articles
            for news in res_json['articles']:
                news['source'] = res_json['source']

            articles.extend(res_json['articles'])
    return articles
