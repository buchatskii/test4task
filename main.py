#Задание 5
'''
import random

def get_jokes(joke):
    funny_sentence = ''
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    i = 0
    funny_sentence_nouns = len(nouns) - 1
    funny_sentence_adverbs = len(adverbs) - 1
    funny_sentence_adjectives = len(adjectives) - 1
    while i < joke:
        funny_word_nouns = nouns[random.randint(0, funny_sentence_nouns)]
        funny_word_adverbs = adverbs[random.randint(0, funny_sentence_adverbs)]
        funny_word_adjectives = adjectives[random.randint(0, funny_sentence_adjectives)]
        funny_sentence += funny_word_nouns + " " + funny_word_adverbs + " " + \
                                 funny_word_adjectives + " " + '\n'
        i += 1
    return funny_sentence

if __name__ == '__main__':
    joke = int(input("Сколько шуток про тарабан вы хотите?\n"))
    jokes = get_jokes(joke)
    print(jokes)
'''
#Задание 3
'''
def thesaurus(*names):
    vocabulary = {}
    for name in names:
        letter = name[0]
        if vocabulary.get(letter) == None:
            vocabulary.update({str(letter): name})
        else:
            vocabulary[letter] += ", " + name
    return vocabulary

if __name__ == '__main__':
    massive = thesaurus("Фахид", "Мария", "Петр", "Илья")
    print(str(massive))
'''
#Задание 1-2
'''
word_book = {'one': 'Один',
             'two': 'Два',
             'three': 'Три',
             'four': 'Четыре',
             'five': 'Пять',
             'six': 'Шесть',
             'seven': 'Семь',
             'eigh': 'Восемь',
             'nine': 'Девять',
             'ten': 'Десять'}

b = input("Введите число по англ.\n")
double_word_book = str(b).lower()
try:
    if b.istitle():
        print(str(word_book[double_word_book]).title())
    else:
        print(str(word_book[double_word_book]).lower())
except KeyError:
    print("None")
'''