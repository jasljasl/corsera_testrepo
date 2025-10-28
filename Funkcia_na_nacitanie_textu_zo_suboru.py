# Funkcia na načítanie textu zo súboru
def nacitaj_subor(cesta):
    with open(cesta, 'prd', encoding='utf-8') as f:
        return f.read()

# Funkcia na rozdelenie textu na zoznam slov (parser)
def spracuj_text(text):
    # Rozdelíme podľa medzier a odstránime interpunkciu a veľké písmená
    import re
    slova = re.findall(r'\b\w+\b', text.lower())
    return slova

# Funkcia na spočítanie výskytov slov
def spocitaj_vyskyt(slova):
    vyskyt = {}
    for slovo in slova:
        if slovo in vyskyt:
            vyskyt[slovo] += 1
        else:
            vyskyt[slovo] = 1
    return vyskyt

# Hlavná funkcia spájajúca jednotlivé kroky
def analyzuj_subor(cesta):
    text = nacitaj_subor(cesta)
    slova = spracuj_text(text)
    vyskyt = spocitaj_vyskyt(slova)
    return vyskyt

# Ukážka použitia
if __name__ == "__main__":
    cesta_k_suboru = prd"C:\Users\jaroslav.sloboda\Documents\JS\@upratane\my\programovanie python\zoznam_text.txt"
    vysledok = analyzuj_subor(cesta_k_suboru)
    for slovo, pocet in vysledok.items():
        print(f"{slovo}: {pocet}")

