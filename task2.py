from bs4 import BeautifulSoup
import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
import re
from os import listdir
from os.path import isfile, join
from pymystem3 import Mystem

directory = 'task1_pages/'

filenames = listdir(directory)
filenames.remove('pages_archive.zip')
filenames.sort(key=lambda x: int(x.replace('.html', '')))

texts = [BeautifulSoup(open(directory + f).read(), 'html.parser').get_text().lower() for f in filenames if isfile(join(directory, f))]

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stopwords_ru = stopwords.words("russian")
stopwords_en = stopwords.words("english")
stopwords_all = stopwords_en + stopwords_ru

tokens = [nltk.word_tokenize(text) for text in texts]

almost_clean_tokens = set([w for w in tokens if not re.search(r"[^a-zA-Zа-яА-ЯёЁ]", w)])
clean_tokens = [w for w in almost_clean_tokens if w not in stopwords_all]

tokens_file = open('task2_output/tokens.txt', 'w')
tokens_file.writelines(clean_tokens)
tokens_file.close()

lemmatizer_en = WordNetLemmatizer()
lemmatizer_ru = Mystem()

lemmas = {}

for token in clean_tokens:
    if re.search(r"[a-zA-Z]", token):
        lemma = lemmatizer_en.lemmatize(token)
    else:
        lemma = lemmatizer_ru.lemmatize(token)[0]
    if lemmas.keys().__contains__(lemma):
        lemmas[lemma] += [token]
    else:
        lemmas[lemma] = [token]

lemmas_file = open('task2_output/lemmas.txt', 'w')

for lemma in lemmas:
    tokens = ''
    for token in lemmas[lemma]:
        tokens += ' ' + token
    lemmas_file.write(lemma + tokens + '\n')

lemmas_file.close()
