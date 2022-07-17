import random


def create_element_list(record, choice_user):
    element_list = []
    for element in record:
        row = element.replace('\n', '').split('-')
        if row[0].rstrip() == choice_user:
            element_list.append(row[1])
    return element_list


def user_choice():
    user_choice = input('Wybierz kategorię: ')
    return user_choice


def is_category_exists(element):
    if len(element) > 0:
        return 1
    else:
        return 0


def game_element():
    game_list = []
    while True:
        element_list = create_element_list(record_list, user_choice())
        if is_category_exists(element_list) == 0:
            print("Taka kategoria nie istnieje. Spróbuj jeszcze raz")
            continue
        else:
            game_list = element_list
            print("Zaczynamy grę, wybieram słowo")
            break
    return game_list

def game(list_element):
    word = random.choice(list_element).strip()
    letter = list(word)
    looking_word = ['-']*len(letter)
    while True:
        user_word = ""
        for element in looking_word:
            user_word+=element
        print(user_word)
        user_choice = input("Podaj litere: ")
        if user_choice in letter:
            print(f'litera {user_choice} istnieje')
        else:
            print("NIe ma takiej litery")

    print(user_word)








with open('wisielec.txt') as wis:
    record_list = wis.readlines()


def main():
    game_list = game_element()
    game(game_list)

if __name__ == "__main__":
    main()
