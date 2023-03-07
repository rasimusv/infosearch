from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join

# считать токены
tokens_file = open('task2_output/tokens.txt')
index_file = open('task3_output/index.txt', 'w')

directory = 'task1_pages/'
files = [directory + f for f in listdir(directory) if isfile(join(directory, f)) and f != 'pages_archive.zip']
texts = []
index = []

for file in files:
    html = open(file)
    text = BeautifulSoup(html, 'html.parser').get_text()
    texts.append(text)


for token in tokens_file.read().splitlines():
    i = 0
    numbers_of_texts = " "
    for text in texts:
        i = i + 1
        if token in text:
            numbers_of_texts += (str(i) + " ")
    index_file.write(token + numbers_of_texts + '\n')

index_file.close()

