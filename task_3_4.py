def thesaurus_adv(*names_surnames):
    my_list = {}
    for name_surname in names_surnames:
        name, surname = name_surname.split()
        my_list.setdefault(surname[0], {})
        my_list[surname[0]].setdefault(name[0], [])
        my_list[surname[0]][name[0]].append(name_surname)
    sorted_dict = {n: my_list[n] for n in sorted(my_list)}
    return my_list
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))