# a = input("podaj 3 litery")
# k = ""
# for i in range(3):
#  k = str(ord(a[i])+i*2+1)
# print(k)
#Tworzenie planszy do gry
# plansza = [
#     [' ',' ',' '],
#     [' ',' ',' '],
#     [' ',' ',' ']
# ]

# #Funkcja wyświetlająca planszę
# def wyswietl_plansze(plansza):
#     for i in plansza:
#         print(i)

# #Funkcja umożliwiająca graczowi wybór pola
# def wybierz_pole(plansza, gracz):
    
#     #Pętla sprawdzająca, czy gracz wybrał prawidłowe pole
#     while True:
#         wiersz = int(input(f"Gracz {gracz}. Wybierz wiersz (1-3): "))
#         kolumna = int(input(f"Gracz {gracz}. Wybierz kolumnę (1-3): "))
#         if wiersz < 1 or wiersz > 3 or kolumna < 1 or kolumna > 3:
#             print("Nieprawidłowe pole! Spróbuj ponownie.")
#             continue
#         if plansza[wiersz-1][kolumna-1] != ' ':
#             print("To pole jest już zajęte! Spróbuj ponownie.")
#             continue
#         break

#     #Ustawienie znaku gracza na wybranym polu
#     plansza[wiersz-1][kolumna-1] = gracz

# #Funkcja sprawdzająca, czy któryś z graczy wygrał
# def czy_wygrana(plansza, gracz):
    
#     #Sprawdzenie wierszy
#     for wiersz in plansza:
#         if wiersz.count(gracz) == 3:
#             return True
    
#     #Sprawdzenie kolumn
#     for i in range(3):
#         kolumna = [wiersz[i] for wiersz in plansza]
#         if kolumna.count(gracz) == 3:
#             return True
    
#     #Sprawdzenie przekątnych
#     if plansza[0][0] == gracz and plansza[1][1] == gracz and plansza[2][2] == gracz:
#         return True
#     if plansza[0][2] == gracz and plansza[1][1] == gracz and plansza[2][0] == gracz:
#         return True
    
#     #Jeżeli żaden z graczy nie wygrał, zwróć False
#     return False

# #Główna pętla gry
# while True:
#     #Wyświetlenie planszy
#     wyswietl_plansze(plansza)

#     #Ruch gracza X
#     wybierz_pole(plansza, 'X')
#     wyswietl_plansze(plansza)

#     #Sprawdzenie, czy gracz X wygrał
#     if czy_wygrana(plansza, 'X'):
#         print("Gracz X wygrał!")
#         break

#     #Sprawdzenie, czy na planszy nie ma już wolnych pól
#     if not any(' ' in wiersz for wiersz in plansza):
#         print("Remis!")
#         break

#     #Ruch gracza O
#     wybierz_pole(plansza, 'O')
#     wyswietl_plansze(plansza)

#     #Sprawdzenie, czy gracz O wygrał
#     if czy_wygrana(plansza, 'O'):
#         print("Gracz O wygrał!")
#         break
n=int(input("Podaj ile liczb nieparzystych:"))
for i in range(1,n*2+1,2):
  print(i*i)