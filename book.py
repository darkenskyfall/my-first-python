
books = []

def show_data():
    if len(books) <= 0:
        print("There is no books!")
    else:
        for index in range(len(books)):
            print(index, books[index])

def insert_data():
    new_book = input("Insert a new book : ")
    books.append(new_book)

def edit_data():
    show_data()
    index = int(input("Please insert index of book : "))
    if (index > len(books)):
        print("Wrong index of book")
    else:
        new_title = input("Insert new title : ")
        books[index] = new_title

def delete_data():
    show_data()
    index = int(input("Please insert index of book : "))
    if (index > len(books)):
        print("Wrong index of book")
    else:
        books.remove(books[index])

def show_menu():
    print("\n")
    print("----------Menu----------")
    print(" [1] Show Data ")
    print(" [2] Insert Data ")
    print(" [3] Edit Data ")
    print(" [4] Delete Data ")
    print(" [5] Exit ")

    menu = int(input("Pilih Menu : "))
    print("\n")

    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print("Salah Pilih !")

if __name__ == "__main__":

    while(True):
        show_menu()

# buku_undangan = []

# def input_tamu():
#     nama_tamu = input("Masukkan nama tamu : ")
#     buku_undangan.append(nama_tamu)
#     for index in range(len(buku_undangan)):
#         print(buku_undangan[index])

# if __name__ == "__main__":
    
#     while(True):
#         input_tamu()