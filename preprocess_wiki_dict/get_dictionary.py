import warnings
import nltk
import re
from urllib.parse import unquote
import pandas as pd
from bs4 import BeautifulSoup
import sys

nltk.download('punkt')


def remove_title(article):
    return BeautifulSoup(re.sub(r'^.*?\n', '', article)).text


def get_href(sentences):
    href_links = []
    for sentence in sentences:
        soup = BeautifulSoup(sentence)
        links = [unquote(a['href'])
                 for a in soup.find_all('a') if a.has_attr('href')]
        href_links.append(links)
    return href_links


def translate_links(list_of_links, df):
    def translate_to_english(title, df):
        try:
            return df[df['ll_from_title'] == title]['ll_title'].values[0]
        except:
            return None
    res = [translate_to_english(link, df) for link in list_of_links]
    return set([i for i in res if i])


def similar_sentences(sentences_1, href_links_1, sentences_2, href_links_2, threshold=2):
    """Summary or Description of the Function

    Parameters:
    sentences_1 list(string): A list of sentences
    href_links_1 list(list(string)): A list of url from the sentences
    sentences_2 list(string): A list of sentences
    href_links_2 list(list(string)): A list of url from the sentences

    Returns:
    list: a list of tuples of sentences with common
    """
    returned_sentence_pair = []
    for sent_1, links_1 in zip(sentences_1, href_links_1):
        if len(links_1):
            for sent_2, links_2 in zip(sentences_2, href_links_2):
                if len(links_2):
                    if len(links_1.intersection(links_2)) >= threshold:
                        returned_sentence_pair.append((sent_1, sent_2))
                        break
    return returned_sentence_pair


language = sys.argv[1]
warnings.filterwarnings("ignore")
df = pd.read_csv(f'{language}_full_paragraph.csv')
df_title = pd.read_csv(f'{language}_title.csv')
df_clean = df.dropna().drop_duplicates()
df_clean['cleaned_source'] = df_clean['source_paragraph'].apply(remove_title)
df_clean['cleaned_target'] = df_clean['target_paragraph'].apply(remove_title)
source_sentences = df_clean['cleaned_source'].apply(
    nltk.tokenize.sent_tokenize)
target_sentences = df_clean['cleaned_target'].apply(
    nltk.tokenize.sent_tokenize)
source_flat_list = [item for sublist in source_sentences for item in sublist]
target_flat_list = [item for sublist in target_sentences for item in sublist]
print(len(source_flat_list))
print(len(target_flat_list))
with open(f'{language}.{language}', 'w') as f:
    for item in source_flat_list:
        f.write("%s\n" % item.replace('\n', ' '))
with open(f'{language}.english', 'w') as f:
    for item in target_flat_list:
        f.write("%s\n" % item.replace('\n', ' '))
