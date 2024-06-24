# Інформація про користувача
reader_info = {
    "ID": 1,
    "Прізвище": "Строїч",
    "Ім'я": "Олександр",
    "Група": "ІПЗс-21-1",
    "Курс": 3,
    "Книги": [],
    "Статистика книг": []
}

print("\nКарта читача:")
print("ID:", reader_info["ID"])
print("Прізвище:", reader_info["Прізвище"])
print("Ім'я:", reader_info["Ім'я"])
print("Група:", reader_info["Група"])
print("Курс:", reader_info["Курс"])
print("Книги у боргу:", reader_info["Книги"])
print("Статистика книг:", reader_info["Статистика книг"])

# Головний цикл програми
while True:
    print("\nМеню:")
    print("1. Вивести карту читача")
    print("2. Взяти книгу")
    print("3. Повернути книгу")
    print("0. Вихід")
    
    choice = input("Виберіть опцію: ")

    if choice == "1":
        print("\nКарта читача:")
        print("ID:", reader_info["ID"])
        print("Прізвище:", reader_info["Прізвище"])
        print("Ім'я:", reader_info["Ім'я"])
        print("Група:", reader_info["Група"])
        print("Курс:", reader_info["Курс"])
        print("Книги у боргу:", reader_info["Книги"])
        print("Статистика книг:", reader_info["Статистика книг"])

    elif choice == "2":
        book_title = input("Введіть назву книги, яку ви хочете взяти: ")
        reader_info["Книги"].append(book_title)
        print(f"Книга '{book_title}' успішно додана до списку борг.")

    elif choice == "3":
        borrowed_books = reader_info["Книги"]
        if borrowed_books:
            print("Книги у боргу:", borrowed_books)
            book_to_return = input("Введіть назву книги, яку ви хочете повернути: ")
            if book_to_return in borrowed_books:
                reader_info["Книги"].remove(book_to_return)
                reader_info["Статистика книг"].append(book_to_return)
                print(f"Книга '{book_to_return}' успішно повернена.")
            else:
                print("Ви не маєте такої книги у боргу.")
        else:
            print("У вас немає книг у боргу.")

    elif choice == "0":
        print("Дякую за використання програми!")
        break

    else:
        print("Некоректний вибір опції. Спробуйте ще раз.")
