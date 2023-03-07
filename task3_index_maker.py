from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join

# считать токены
tokens_file = open('task2_output/tokens.txt')
index_file = open('task3_output/index.txt', 'w')

directory = 'task1_pages/'

filenames = listdir(directory)
filenames.remove('pages_archive.zip')
filenames.sort(key=lambda x: int(x.replace('.html', '')))

files = [open(directory + f) for f in filenames if isfile(join(directory, f))]

texts = []
index = []

for file in files:
    text = BeautifulSoup(file, 'html.parser').get_text().lower()
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

