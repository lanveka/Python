class print_edition:
    def __init__(self, name, pageCount, izdat):
        self.__name = name
        self.__pageCount = pageCount
        self.__izdat = izdat

    @property
    def name(self) :
        return self.__name

    @property
    def pageCount(self) :
        return self.__pageCount

    @property
    def izdat(self) :
       return self.__izdat

    def display_info(self):
        print("Название издания: ", self.__name, "\tКоличество страниц:", self.__pageCount,
              "\tИздательство: ", self.__izdat)
class book(print_edition):
   def avtor(self,author):
        print("Название книги:   ", self.name,  "\tАвтор: ", author)

class magazine(print_edition):
   def mag(self, period):
       print("Название журнала: ", self.name, "\tПериодичность ", period)

class textbook(book) :
    def textbk(self, subject):
        print("Учебное пособие по предмету: ", subject, "\tКоличество страниц:", self.pageCount,
              "\tИздательство: ", self.izdat)

p = book("Пуаро", 358, "DD")
p.avtor("Агата Кристи")
p.display_info()
print("______________________________________")
d = magazine("Vogue", 150, "Condé Nast Publications")
d.mag("ежемесячный")
d.display_info()
print("_____________________________________")
y = textbook("Учебное пособие", 80, "MO")
y.textbk("Химия")
y.display_info()