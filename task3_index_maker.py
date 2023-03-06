from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join

# считать токены
tokens_file = open('task2_output/tokens.txt', encoding='iso8859_1')
index_file = open('task3_output/index.txt', 'w', encoding='iso8859_1')

directory = 'task1_pages/'
files = [directory + f for f in listdir(directory) if isfile(join(directory, f))]
texts = []
index = []

for file in files:
    html = open(file, encoding='iso8859_1')
    text = BeautifulSoup(html, 'html.parser').get_text()
    texts.append(text)


for token in tokens_file.read().splitlines():
    i = 0
    numbers_of_texts = " "
    for text in texts:
        i = i + 1
        if token in text:
            numbers_of_texts += (str(i) + " ")
    if numbers_of_texts != " ":
        index_file.write(token + numbers_of_texts + '\n')

index_file.close()

