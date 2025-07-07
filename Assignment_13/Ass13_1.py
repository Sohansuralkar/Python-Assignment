class BookStore:
    NoOfBooks = 0
    def __init__(self):
        self.name = input("please Enter the number of books :")
        self.Author = input("Please Enter amount of Book : ")
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(self.name + "by" + self.Author)
        print("Number of Books : ", BookStore.NoOfBooks)

    def main(self):
        self.Display()

if __name__ == "__main__":
    obj1 = BookStore()
    obj1.main()
    obj2 = BookStore()
    obj2.main()