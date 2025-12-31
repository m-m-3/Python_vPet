import os
from pet import Pet

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("Wciśnij Enter, aby wrócić do menu...")

def read_option(max_value):
    while True:
        raw = input("Wybierz opcję: ")
        try:
            value = int(raw)
        except ValueError:
            print(f"Niepoprawny wybór. Podaj liczbę 0-{max_value}.")
            continue

        if 0 <= value <= max_value:
            return value

        print(f"Niepoprawny wybór. Podaj liczbę 0-{max_value}.")

def spend_time_menu(pet):
    clear()
    print("===== SPĘDŹ CZAS =====")
    print("1. Krótka przerwa")
    print("2. Drzemka")
    print("3. Spanie")
    print("4. Spacer")
    print("0. Wróć")

    choice = read_option(4)
    if choice == 0:
        return

    pet.SpendTime(choice)
    print("Statystyki po aktywności:")
    print(pet.Status)
    pause()

def main():
    clear()
    print("===== WIRTUALNE ZWIERZĄTKO =====")
    pet_name = input("Podaj imię zwierzątka: ") or ""
    pet = Pet(Name=pet_name)

    while True:
        clear()
        print(f"===== {pet.Name} =====")
        print("1. Statystyki")
        print("2. Nakarm")
        print("3. Pobaw się")
        print("4. Spędź czas")
        print("0. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            print(pet.Status)
            pause()
        elif choice == "2":
            print("TODO: Karmienie")
            pause()
        elif choice == "3":
            print("TODO: Zabawa")
            pause()
        elif choice == "4":
            spend_time_menu(pet)
        elif choice == "0":
            return
        else:
            print("Niepoprawny wybór.")
            pause()

if __name__ == "__main__":
    main()