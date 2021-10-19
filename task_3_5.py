import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
def get_jokes(number):
    my_list = []
    for n in range(number):
        cur_nouns = random.choice(nouns)
        cur_adverbs = random.choice(adverbs)
        cur_adjectives = random.choice(adjectives)
        my_list.append(f'{cur_nouns} {cur_adverbs} {cur_adjectives}')
    return my_list
print(get_jokes(2))