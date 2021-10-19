def thesaurus(*names):
    my_list = {}
    for name in names:
        my_list.setdefault(name[0], [])
        my_list[name[0]].append(name)
    return my_list
print(thesaurus("Иван", "Мария", "Петр", "Илья"))