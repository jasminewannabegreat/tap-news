import os
import sys
from newspaper import Article
# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'scrapers'))

import cnn_news_scraper
from cloudAMQP_client import CloudAMQPClient

# TODO: use your own queue.
DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://lkvdaice:i_Z8qrNq8jeRuiNSYb3WKWG35PX-IY4G@donkey.rmq.cloudamqp.com/lkvdaice"
DEDUPE_NEWS_TASK_QUEUE_NAME = "tap-news-deduper-news-task-queue"
SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://gnjkwrcm:wuIt26fgg3yjHAipAm7vV--KmcHV9ArE@donkey.rmq.cloudamqp.com/gnjkwrcm"
SCRAPE_NEWS_TASK_QUEUE_NAME = "test"

SLEEP_TIME_IN_SECONDS = 5

dedupe_news_queue_client = CloudAMQPClient(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
scrape_news_queue_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

def handle_message(msg):
    if msg is None or not isinstance(msg,dict):
        print'message is broken'
        return
    task = msg
    text = None

    article = Article(task['url'])
    article.download()
    article.parse()

    task['text'] = article.text.encode('utf-8')

    dedupe_news_queue_client.sendMessage(task)  
    # task
    # if task['source'] == 'cnn':
    #     print 'scapping CNN news'
    #     text = cnn_news_scraper.extract_news(task['url'])
    # else:
    #     print "News source [%s] is not supported." %task['source']
    
    # task['text'] = text
    # dedupe_news_queue_client.sendMessage(task)

while True:
    if scrape_news_queue_client is not None:
        msg = scrape_news_queue_client.getMessage()
        if msg is not None:
            try:
                handle_message(msg)
            except Exception as e:
                print 
                pass
        scrape_news_queue_client.sleep(SLEEP_TIME_IN_SECONDS)