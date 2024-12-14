def dictionary_of_words (text: str) -> dict:
    words = text.split()
    word_count = {}

    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

if __name__ == '__main__':
    text = str(input('Введите слова через пробел: '))
    print(dictionary_of_words(text))
    