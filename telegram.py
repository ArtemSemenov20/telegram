# міні проєкт робота з файлами
def load_shopping_list(file_path):
    try:
        with open(file_path, 'r') as file:
            shopping_list = [line.strip().split(', ') for line in file.readlines()]
        return shopping_list
    except FileNotFoundError:
        return []


def save_shopping_list(file_path, shopping_list):
    with open(file_path, 'w') as file:
        for item in shopping_list:
            file.write(', '.join(item) + '\n')


def display_shopping_list(shopping_list):
    if not shopping_list:
        print("ваш список покупок пустий ;( ")
    else:
        print("cписок покупок:")
        for item in shopping_list:
            print(f"{item[0]}: {item[1]} од.")


def add_item(shopping_list):
    name = input("напишіть назву продукта: ")
    quantity = input("введіть кількість продукта(ів): ")
    shopping_list.append([name, quantity])
    print(f"{name} додано до списку покупок")


def edit_item(shopping_list):
    display_shopping_list(shopping_list)
    index = int(input("введіть номер продукту який треба відредагувати: ")) - 1
    if 0 <= index < len(shopping_list):
        new_quantity = input("введіть нову кількість продукту: ")
        shopping_list[index][1] = new_quantity
        print(f"кількість продукту оновлено.")
    else:
        print("не правдивий номер продукту ;( ")


def remove_item(shopping_list):
    display_shopping_list(shopping_list)
    index = int(input(" напишіть номер продукту, який потрібно видалити: ")) - 1
    if 0 <= index < len(shopping_list):
        removed_item = shopping_list.pop(index)
        print(f"{removed_item[0]} видалено зі списку покупок")
    else:
        print("не правдивий номер продукту")


if __name__ == "__main__":
    file_path = "shopping_list.txt"
    shopping_list = load_shopping_list(file_path)

while True:
    print("\nМеню:")
    print("1. передивитися список покупок")
    print("2. добавити продукт до списку")
    print("3. редагувати кількість продукту(ів)")
    print("4. видалити продукт зі списку")
    print("5. іберегти та вийти :3")
    choice = input("виберіть опцію : ")

    if choice == '1':
        display_shopping_list(shopping_list)
    elif choice == '2':
        add_item(shopping_list)
    elif choice == '3':
        edit_item(shopping_list)
    elif choice == '4':
        remove_item(shopping_list)
    elif choice == '5':
        save_shopping_list(file_path, shopping_list)
        print("ваші зміни збережено.")
        break
    else:
        print("невірний вибір,будь ласка,виберіть опцію від 1 до 5")
