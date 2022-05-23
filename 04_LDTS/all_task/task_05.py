#-- TASK 5 -- W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.

txt = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

txt = txt.replace("," , " ")
txt = txt.lower()
txt = txt.replace("\n", " ")
new_list = txt.split()

set_word = set(new_list)
list_word = list(set_word)

words_counter = {}

for index in list_word:
    words_counter[index] = new_list.count(index)

print(words_counter)