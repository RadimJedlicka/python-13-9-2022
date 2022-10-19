# TODO importy zakladnich knihoven (modulu)
from random import choice

# TODO importy vlastnich modulu
from slova import hadana_slova
from grafika import obesenec

# TODO promenne
zivoty = 7
hra_bezi = True
slovo = choice(hadana_slova)
tajenka = ['_'] * len(slovo)


while hra_bezi and zivoty > 0:

    # TODO zobraz tajenku
    print(f"Tajenka: {''.join(tajenka)}")

    # TODO input
    hadani = input('Hadej pismeno/cele slovo: ')

    # pokud uzivatel uhadl cele slovo
    if hadani == slovo:
        hra_bezi = False

    # pokud uzivatel uhadne pismeno
    elif hadani in slovo and len(hadani) == 1:
        for index, symbol in enumerate(slovo):
            if symbol == hadani:
                tajenka[index] = hadani
        print('Uhodl jsi spravne pismeno!')

        # pokud uzivatel vsechna pismeno po jednom
        if '_' not in tajenka:
            hra_bezi = False
            
    
    # pokud uzivatel uhadl spatne pismeno
    else:
        print('Pismeno neni v tajence, hadej znova!')
        zivoty -= 1
        print(zivoty)

# vypis else po tom, co je while cyklus prerusen
else:
    # kdyz uzivatel vyhral
    if hra_bezi == False:
        print('Vyhral jsi!')
    # kdyz uzivatel prohral
    else:
        print(f'Prohral jsi, tajenka byla {slovo}')
