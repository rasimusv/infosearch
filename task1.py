from bs4 import BeautifulSoup
import requests


def read_from_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    for data in soup(['style', 'script', 'link']):
        data.decompose()
    return str(soup)


directory = "task1_pages"
i = 1
index_file = open("index.txt", "w")

for i in range(1, 101):
    url = "https://ru.wikipedia.org/wiki/" + str(i) + "_год"
    text = read_from_page(url)

    # Запись в файл
    file = open(directory + "/" + str(i) + ".html", "w")
    file.write(text)
    file.close()

    # Запись информации в index.txt
    index_file.write(str(i) + ". " + url + "\n")

    i += 1

index_file.close()
