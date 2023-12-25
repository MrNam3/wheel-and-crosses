def rysuj_plansze(plansza):
    rozmiar = len(plansza)

    # Nagłówki kolumn (od góry)
    print("   " + "   ".join(str(i + 1) for i in range(rozmiar)))

    # Rysowanie planszy
    for i, wiersz in enumerate(reversed(plansza)):
        print("  " + "-----" * rozmiar)
        print(f"{rozmiar - i} |", end="")
        for j, pole in enumerate(wiersz):
            print(f" {pole} |", end="")
        print()

    # Linia oddzielająca na dole planszy
    print("  " + "-----" * rozmiar)
    print()
def utworz_plansze(rozm):
    return [[" " for _ in range(rozm)] for _ in range(rozm)]


def wykonaj_ruch(gracz, plansza):
    while True:
        try:
            wiersz = int(input(f"{gracze[gracz]} ({gracz}), podaj numer wiersza (1, 2, {len(plansza)}): ")) - 1
            kolumna = int(input(f"{gracze[gracz]} ({gracz}), podaj numer kolumny (1, 2, {len(plansza)}): ")) - 1

            if 0 <= wiersz < len(plansza) and 0 <= kolumna < len(plansza) and plansza[wiersz][kolumna] == " ":
                plansza[wiersz][kolumna] = gracz
                ruchy[gracz] += 1
                break
            else:
                print("Nieprawidłowe pole. Wybierz ponownie.")
        except (ValueError, IndexError):
            print("Błędne dane. Podaj poprawne liczby.")


def czyj_ruch(gracz):
    return "O" if gracz == "X" else "X"


def sprawdz_wygrana(gracz, plansza):
    for wiersz in plansza:
        if all(element == gracz for element in wiersz):
            return True

    for kolumna in range(len(plansza)):
        if all(plansza[w][kolumna] == gracz for w in range(len(plansza))):
            return True

    if all(plansza[i][i] == gracz for i in range(len(plansza))) or all(plansza[i][len(plansza) - 1 - i] == gracz for i in range(len(plansza))):
        return True

    return False


def sprawdz_remis(plansza):
    return all(all(element != " " for element in wiersz) for wiersz in plansza)


def czy_kontynuowac():
    odpowiedz = input("Czy chcesz zagrać ponownie? (tak/nie): ").lower()
    return odpowiedz == "tak"


# Dodajemy imiona graczy
gracze = {"X": "", "O": ""}
for gracz in gracze:
    gracze[gracz] = input(f"Podaj imię gracza {gracz}: ")

# Wybór rozmiaru planszy
while True:
    try:
        rozmiar = int(input("Wybierz rozmiar planszy (3, 6, 9): "))
        if rozmiar in [3, 6, 9]:
            break
        else:
            print("Nieprawidłowy rozmiar. Wybierz ponownie.")
    except ValueError:
        print("Błędne dane. Podaj poprawną liczbę.")

plansza = utworz_plansze(rozmiar)
ruchy = {"X": 0, "O": 0}
aktualny_gracz = "X"

while True:
    rysuj_plansze(plansza)
    wykonaj_ruch(aktualny_gracz, plansza)

    if sprawdz_wygrana(aktualny_gracz, plansza):
        print(f"{gracze[aktualny_gracz]} wygrał(a) po {ruchy[aktualny_gracz]} ruchach!")
        if czy_kontynuowac():
            # Wybór rozmiaru planszy
            while True:
                try:
                    rozmiar = int(input("Wybierz rozmiar planszy (3, 6, 9): "))
                    if rozmiar in [3, 6, 9]:
                        break
                    else:
                        print("Nieprawidłowy rozmiar. Wybierz ponownie.")
                except ValueError:
                    print("Błędne dane. Podaj poprawną liczbę.")
            plansza = utworz_plansze(rozmiar)
            ruchy = {"X": 0, "O": 0}
            continue
        else:
            break

    if sprawdz_remis(plansza):
        print("Remis!")
        if czy_kontynuowac():
            # Wybór rozmiaru planszy
            while True:
                try:
                    rozmiar = int(input("Wybierz rozmiar planszy (3, 6, 9): "))
                    if rozmiar in [3, 6, 9]:
                        break
                    else:
                        print("Nieprawidłowy rozmiar. Wybierz ponownie.")
                except ValueError:
                    print("Błędne dane. Podaj poprawną liczbę.")
            plansza = utworz_plansze(rozmiar)
            ruchy = {"X": 0, "O": 0}
            continue
        else:
            break

    aktualny_gracz = czyj_ruch(aktualny_gracz)
