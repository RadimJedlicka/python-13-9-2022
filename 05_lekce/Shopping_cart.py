# TODO promenne
potraviny = {
    'mleko':    [30,  5],    # index 0 -> cena; index 1 -> mnozstvi
    'maso':     [100, 1],
    'banan':    [30, 10],
    'jogurt':   [10,  5],
    'chleb':    [20,  5],
    'jablko':   [10, 10],
    'pomeranc': [15, 10], 
}

nabidka = """
+-----------+----------+
| POTRAVINA |   CENA   |
+-----------+----------+
| mleko     |    30,-  |
| maso      |   100,-  |
| banan     |    30,-  |
| jogurt    |    10,-  |
| chleb     |    20,-  |
| jablko    |    10,-  |
| pomenrac  |    15,-  |
| jablko    |    20,-  |
| grep      |    45,-  |
+-----------+----------+
"""

kosik = {}
# kosik = dict()

oddelovac = '=' * 40

# TODO Pozdrav a vypsani nabidky
print(
    'Vitejte v nasem online nakupnim centru', 
    oddelovac, 
    nabidka, 
    'Zvol si zbozi, pro zaplaceni stiskni "q"', 
    sep='\n')

# TODO cely cyklus
while (zbozi := input('Zadej nazev zbozi:')) != 'q':
    # TODO pokud zbozi nebude v nabidce
    if zbozi not in potraviny:
        print(zbozi, 'bohuzel neni v nabidce')

    # TODO Pokud vybrane neni v nakupnim kosiku
    elif zbozi not in kosik and potraviny[zbozi][1] > 0:
        kosik[zbozi] = [potraviny[zbozi], 1]
        potraviny[zbozi][1] = potraviny[zbozi][1] - 1
        print(kosik)

    # TODO pokud zbozi je v kosiku
    elif zbozi in kosik and potraviny[zbozi][1] > 0:
        kosik[zbozi][1] += 1
        potraviny[zbozi][1] -= 1
        print(kosik)

    # TODO pokud zbozi jiz neni skladem
    elif potraviny[zbozi][1] == 0:
        print(f'{zbozi} jiz neni na sklade')

# TODO vypis kosiku
else:
    print(oddelovac, kosik, sep='\n')
