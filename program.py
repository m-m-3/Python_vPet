import os
from pet import Pet

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("Wciśnij Enter, aby wrócić do menu...")

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
            print("TODO: Statystyki")
            pause()
        elif choice == "2":
            print("TODO: Karmienie")
            pause()
        elif choice == "3":
            print("TODO: Zabawa")
            pause()
        elif choice == "4":
            print("TODO: Spędź czas")
            pause()
        elif choice == "0":
            return
        else:
            print("Niepoprawny wybór.")
            pause()

if __name__ == "__main__":
    main()