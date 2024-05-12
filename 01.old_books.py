book_name = input()

count_book = 0
searching_book = book_name

while book_name != "No More Books":
    book_name = input()
    count_book += 1
    if book_name == searching_book:
        count_book -= 1
        print(f"You checked {count_book} books and found it.")
        break
    elif book_name == "No More Books":
        count_book -= 1

else:
    print(f"The book you search is not here!")
    print(f"You checked {count_book} books.")
