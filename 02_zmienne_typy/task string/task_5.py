# task 5 --- Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok. Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.

txt = input("Wprowadź tekst: ")

reverseTxt = txt[::-1]

verf = txt.lower().replace(" ","") == reverseTxt.lower().replace(" ","")

print(f"Czy tekst '{txt}' jest palindromem? -->", verf)