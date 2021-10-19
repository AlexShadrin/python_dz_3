my_list = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
}
def num_translate_adv(number_en):
    if number_en[0] == number_en[0].upper():
        number_en = number_en.lower()
        return my_list[number_en].capitalize()
    else:
        return my_list[number_en]
print(num_translate_adv('One'))
print(num_translate_adv('two'))