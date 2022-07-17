def uppercase_decorathor(func_txt):
    def upper_letter():
        txt = func_txt()
        return txt.upper()

    return upper_letter

@uppercase_decorathor
def txt_func():
    return 'tekst'


def main():
    print(txt_func())


if __name__ == '__main__':
    main()