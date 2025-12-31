import os
from pet import Pet
from food import Food

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("Wciśnij Enter, aby wrócić do menu...")

def read_option(max_value):
    while True:
        userInput = input("Wybierz opcję: ")
        try:
            value = int(userInput)
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

def feed_menu(pet, foods):
    clear()
    print("===== NAKARM =====")

    for i, food_item in enumerate(foods, start=1):
        print(f"{i}. {food_item.Name} [Głód: -{food_item.ReducesHungerBy}, Energia: +{food_item.AddsEnergy}]")

    print("0. Wróć")
    choice = read_option(len(foods))
    if choice == 0:
        return

    chosen = foods[choice - 1]
    pet.Feed(chosen)

    print(f"Nakarmiono: {chosen.Name}")
    print("Statystyki po karmieniu:")
    print(pet.Status)
    pause()

def main():
    clear()
    print("===== WIRTUALNE ZWIERZĄTKO =====")
    pet_name = input("Podaj imię zwierzątka: ") or ""
    pet = Pet(Name=pet_name)

    foods = [
        Food(Name="Karma sucha", ReducesHungerBy=15, AddsEnergy=10),
        Food(Name="Karma mokra", ReducesHungerBy=30, AddsEnergy=20),
    ]

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
            feed_menu(pet, foods)
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