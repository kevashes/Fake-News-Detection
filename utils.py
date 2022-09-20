# import packages

import numpy as np

from nltk.corpus import stopwords
import string, re, joblib
import requests, random
from bs4 import BeautifulSoup as bs


np.random.seed(419)


# utils
from nltk.stem.porter import PorterStemmer

# turn doc into clean tokens
def cleanDoc(corpus):
    '''
        Turn doc into clean tokens
        
    '''

    all_corpus = []
    for doc in corpus:
        # split into tokens by white space
        tokens = doc.split()
        
        # turn token to lowercase
        tokens = [x.lower() for x in tokens]
                 
        # prepare regex for char filtering
        re_punc = re.compile('[%s]' % re.escape(string.punctuation)) # remove punctuation from each word
        tokens = [re_punc.sub('', w) for w in tokens]
        
        # remove remaining tokens that are not alphabetic
        tokens = [word for word in tokens if word.isalpha()]
        
        # filter out stop words
        stop_words = set(stopwords.words('english'))
        tokens = [w for w in tokens if not w in stop_words]
        
        # stemming of words
        porter = PorterStemmer()
        stemmed = [porter.stem(word) for word in tokens]
        
        # filter out short tokens
        tokens = [word for word in stemmed if len(word) > 1]
        
        all_corpus.append(' '.join(tokens))
    
    return all_corpus



index_2_label = {0:'true', 1:'fake', 2:'neutral'}


def pre_edit(t):
    return ' '.join(t.split()[:30]) 


def make_predictions(query):
    # load saved models
    vec =  joblib.load("../data/unigram_vectorizer.bin")
    model = joblib.load("../data/unigram_mnb.bin")
    print(query)
    p_query = cleanDoc([query])
    print('p_query', p_query)
    cleaned_query = pre_edit(p_query[0])
    print('cleaned_query->', cleaned_query)

    query_vec = vec.transform([cleaned_query])
    # print('query_vec:',query_vec)
    pred = model.predict(query_vec).item()
    print('pred:->', pred)
    return index_2_label[pred]
            
  


# scraper
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

# bbc


def scrape_bbc():
    class_ = 'gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary gs-u-display-none gs-u-display-block@l'

    URL = "https://www.bbc.com/news/world"
    page = requests.get(URL, headers=headers)
    soup = bs(page.content, "html.parser")
    results = soup.find_all("p",class_=class_)
    corpus = [r.text for r in results ]
    random.shuffle(corpus)

    return corpus

def scrape_politifact():
    class_ = 'm-statement__quote'

    URL = 'https://www.politifact.com/'
    page = requests.get(URL, headers=headers)
    soup = bs(page.content, "html.parser")
    results =  soup.find_all("div",class_=class_)
    corpus = [ r.text.strip() for r in results ]
    random.shuffle(corpus)

    return corpus


def scrape_21cpw():
    class_ = 'entry-content clearfix'

    URL = 'https://www.21cpw.com/shock-poll-trump-blue-collar-support-highest-since-fdr-in-1930s/'
    page = requests.get(URL, headers=headers)
    soup = bs(page.content, "html.parser")
    results =  soup.find_all("div",class_=class_)
    corpus = [r.text.strip() for r in results ][0].split('\n')
    random.shuffle(corpus)

    return corpus