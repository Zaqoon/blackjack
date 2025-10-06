import random
from typing import List


class Spiller:
    def __init__(self, navn: str):
        self.navn = navn
        self.score = 0
        self.forfeited = False

    def trekk_kort(self):
        kort = random.randint(1, 10)
        print(f"{self.navn} trekker et kort: {kort}.")
        self.score += kort

    def valider_score(self):
        if self.score > 21:
            print(f"{self.navn} er ute av spillet med {self.score} poeng!")
            return False
        return True


class Game:
    players: List[Spiller]

    def __init__(self):
        self.spillere = []
        self.spill_sekvens()

    def legg_til_spillere(self):
        num_spillere = int(input("Skriv inn antall spillere: "))
        for i in range(num_spillere):
            navn = input(f"Hva heter spiller nummer {i + 1}: ")
            self.spillere.append(Spiller(navn))

    def ny_runde(self):
        for player in self.spillere:
            if not player.forfeited:
                while True:
                    request = input(f"{player.navn} ({player.score}), skriv 'J' for å trekke et kort eller 'N' for pass: ")
                    if request.upper() == 'J':
                        player.trekk_kort()
                        if not player.valider_score():
                            player.forfeited = True
                    elif request.upper() == 'N':
                        print(f"{player.navn} trekker seg.")
                        player.forfeited = True
                    else:
                        print("Ugyldig input, prøv igjen.")
                        continue
                    break

    def finn_vinner(self):
        valid_spillere = [p for p in self.spillere if p.valider_score()]
        if not valid_spillere:
            print("Alle spillere har tapt!")
            return
        vinner = max(valid_spillere, key=lambda p: p.score)
        vinner_liste = [p for p in valid_spillere if p.score == vinner.score]
        if len(vinner_liste) > 1:
            print(f"Det er uavgjort mellom: {', '.join(p.navn for p in vinner_liste)} med {vinner.score} poeng!")
        else:
            print(f"Vinneren er {vinner.navn} med {vinner.score} poeng!")

    def spill_sekvens(self):
        self.legg_til_spillere()
        while any(not player.forfeited for player in self.spillere):
            self.ny_runde()
        self.finn_vinner()


if __name__ == "__main__":
    Game()
