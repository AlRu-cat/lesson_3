# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов, взятых
# из трёх списков:
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
#         Например:
#
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое
# слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


a = input('Введите количество шуток: ')





def get_jokes(a):

    a = int(a)

    # from random import randrange
    #
    # list_of_jokes = []
    # for i in range(a):
    #
    #     joke = []
    #
    #     random_idx = randrange(len(nouns))
    #     word1 = nouns[random_idx]
    #     joke.append(word1)
    #
    #     random_idx = randrange(len(adverbs))
    #     word2 = adverbs[random_idx]
    #     joke.append(word2)
    #
    #     random_idx = randrange(len(adjectives))
    #     word3 = adjectives[random_idx]
    #     joke.append(word3)
    #
    #     finished_joke = ' '.join(joke)
    #
    #     list_of_jokes.append(finished_joke)
    #     i += 1
    #
    # print(list_of_jokes)

    other_jokes = []
    for i in range(a):
        from random import choice
        joke = []
        word1 = choice(nouns)
        word2 = choice(adverbs)
        word3 = choice(adjectives)

        joke.append(word1)
        joke.append(word2)
        joke.append(word3)

        finished_joke = ' '.join(joke)
        i += 1

        other_jokes.append(finished_joke)


    print(other_jokes)

get_jokes(a)
