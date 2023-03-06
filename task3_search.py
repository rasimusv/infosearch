import nltk


def find_request(search_str, d: dict):
    words = search_str.split()
    words_len = len(words)

    all_texts_set = set()
    for i in range(1, 101):
        all_texts_set.add(i)

    res_before_or = []

    if words[0] == 'AND' or words[0] == 'OR':
        return 'It start from AND or OR'

    i = -1

    prev_word = 'OR'
    while i + 1 < words_len:
        i += 1
        word = words[i]
        if (word == 'AND' or word == 'OR') and (prev_word == 'OR' or prev_word == 'AND'):
            return 'ERROR: AND or OR is too clear'

        if word == 'AND' or word == 'OR':
            prev_word = word
            continue

        if i + 1 == words_len and (word == 'AND' or word == 'OR' or word == 'NOT'):
            return 'ERROR: Last word is AND or OR or NOT'

        if word == 'NOT':
            i += 1
            word = words[i]
            if word == 'OR' or word == 'YES' or word == 'NOT':
                return 'ERROR: NO or YES or NOT after NOT'

            texts_for_word = all_texts_set.difference(d.get(word))

        else:
            word = nltk.word_tokenize(word)[0]
            texts_for_word = d.get(word)

        if prev_word == 'AND':
            last_res = res_before_or.pop()
            res_before_or.append(last_res.intersection(texts_for_word))
        elif prev_word == 'OR':
            res_before_or.append(texts_for_word)
        else:
            return 'It is not AND or OR between words'

        prev_word = word

    res = set()
    for i in res_before_or:
        res = res.union(i)

    return res


# Можно задать самостоятельно
search_string = 'NOT кампании AND сю OR зелотов'
d = {}
index_file = open('task3_output/index.txt')
for index in index_file.read().splitlines():
    word = index.split()
    d[word[0]] = set([int(i) for i in word[1:]])
print(d)

d = {'кампании': {8, 54},
     'зелотов': {64},
     'сю': {1, 2, 3, 4, 5, 6, 7, 8}}

print(find_request(search_string, d))
