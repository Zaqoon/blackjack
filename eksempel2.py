import random


SPILLERE = {}

def legg_til_spiller(spiller_id):
    navn = input(f"Skriv inn navnet på spiller {spiller_id + 1}: ")
    SPILLERE[navn] = {
        'poeng': 0,
        'ute': False
    }

def fjern_spiller(navn):
    if navn in SPILLERE:
        del SPILLERE[navn]

def valider_spiller(navn):
    if SPILLERE[navn]['poeng'] > 21:
        SPILLERE[navn]['ute'] = True
        return False
    return True

def fyll_inn_spillere():
    def spiller_antall():
        try:
            antall = int(input("Hvor mange spillere skal være med? "))
            if antall < 1:
                print("Antall spillere må være minst 1.")
                return spiller_antall()
            return antall
        except ValueError:
            print("Vennligst skriv inn et gyldig tall.")
            return spiller_antall()

    antall_spillere = spiller_antall()
    for i in range(antall_spillere):
        legg_til_spiller(i)

def trekk_kort(navn):
    kort = random.randint(1, 10)
    print(f"{navn} trekker et kort: {kort}")
    SPILLERE[navn]['poeng'] += kort
    validering = valider_spiller(navn)
    if not validering:
        print(f"{navn} har nå {SPILLERE[navn]['poeng']} poeng og har tapt!")
        SPILLERE[navn]['poeng'] = 0

def finn_vinner():
    hoyest_poeng = max((spiller['poeng'] for spiller in SPILLERE.values()))
    vinnere = []
    for spiller in SPILLERE:
        if SPILLERE[spiller]['poeng'] == hoyest_poeng:
            vinnere.append(spiller)

    if len(vinnere) > 1:
        print(f"Det er uavgjort mellom: {', '.join(vinnere)} med {hoyest_poeng} poeng hver!")
    else:
        print(f"Vinneren er {vinnere[0]} med {hoyest_poeng} poeng!")

def main():
    fyll_inn_spillere()
    while True:
        for navn in SPILLERE:
            if SPILLERE[navn]['ute']:
                continue
            handling = input(f"{navn} ({SPILLERE[navn]['poeng']}), vil du trekke et kort? (j/n): ")
            if handling.lower() == 'j':
                trekk_kort(navn)
            elif handling.lower() == 'n':
                print(f"{navn} velger å stå med {SPILLERE[navn]['poeng']} poeng.")
                SPILLERE[navn]['ute'] = True
            else:
                print("Ugyldig valg, vennligst skriv 'j' eller 'n'.")
        if all(spiller['ute'] for spiller in SPILLERE.values()):
            print("Spillet er over.")
            finn_vinner()
            break


if __name__ == "__main__":
    main()
