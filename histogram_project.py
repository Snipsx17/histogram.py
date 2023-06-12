from data_processing import compress
# TIPOS
Word = str
Words = list[str]
Totals = dict[str:int]
Histogram = dict[str:float]

# FUNCIONES


def normalize_text(text: str) -> str:
    from unicodedata import normalize
    from string import punctuation as punctuation
    new_text = text.rstrip().strip()
    new_text = normalize('NFKD', new_text).encode(
        'ASCII', 'ignore')
    new_text = ''.join(
        [i for i in text if i not in punctuation])
    return new_text.lower()


def count_words(words_list: Words, stop_words: Words) -> Totals:
    counted_words = Totals()
    for word in words_list:
        if word not in stop_words:
            if word not in counted_words:
                counted_words[word] = 1
            else:
                counted_words[word] += 1
    return counted_words


def histogram(word_listed, grand_total):
    histogram = Histogram()
    for word in word_listed:
        histogram[word] = word_listed[word] / grand_total
    return histogram


if __name__ == '__main__':
    # DECLARACIONES
    full_text = open('alice_full_text.txt', 'r').read()
    full_text = normalize_text(full_text).split()
    stop_words = open('stopwords.txt', 'r').read().split()
    total_words = count_words(full_text, stop_words)
    grand_total = compress(total_words, 0, lambda total,
                           word: total + total_words[word])
    new_histogram = histogram(total_words, grand_total)
    print(new_histogram)
