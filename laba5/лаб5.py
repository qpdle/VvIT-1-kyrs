class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return "Название книги: {}, Автор: {}, Год издания: {}".format(self.title, self.author, self.year)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return "Радиус равен - {}".format(self.radius)

    def set_radius(self, radius):
        try:
            if radius > 0:
                self.radius = radius
        except:
            print("неправильно введен радиус")

kniga = Book("Lord of the rings", "J.R.R. Tolkien", "1954")
print(kniga.get_info())

krug = Circle(15)
krug.set_radius(51)
print(krug.get_radius())
