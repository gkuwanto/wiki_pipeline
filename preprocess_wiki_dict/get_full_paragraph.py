import pickle
import sys
import nltk
import re
from bs4 import BeautifulSoup

with open(sys.argv[1], 'rb') as handle:
    dic = pickle.load(handle)


def remove_title(article):
    return re.sub(r'^.*?\n', '', article)


sentences = [nltk.tokenize.sent_tokenize(BeautifulSoup(
    remove_title(article)).text) for article in dic['first_paragraph']]

flatten = [item for sublist in sentences for item in sublist]

clean_flatten = [item.strip().replace('\n', ' ')
                 for item in flatten if len(item.split()) > 1]
with open(sys.argv[2], 'w') as f:
    for item in clean_flatten:
        f.write('%s\n' % item)
print(len(flatten))
