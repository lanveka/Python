class airline:
    __dest = ''
    __number = ''
    __time = ''
    __days = 0
    __type = ''

    def __init__(self, dest0, number0, time0, days0, type0) :
        self.__dest = dest0
        self.__number = number0
        self.__time = time0
        self.__days = days0
        self.__type = type0
        print('New object created!')

    def get_dest(self) :
        return self.__dest
    def get_number(self) :
        return self.__number
    def get_time(self) :
        return self.__time
    def get_days(self) :
        return self.__days
    def get_type(self) :
        return self.__type


def InfoOut(i):
    print('Пункт назначения: ' + flight[i].get_dest())
    print('Рейс ' + flight[i].get_number())
    print('Вылет ' + flight[i].get_time())
    print('Дни недели '+ str(flight[i].get_days()))
    print('Тип самолета ' + flight[i].get_type())
    print('---------------')


i = 0
flight = [airline('Стокгольм', 'B2 0855', '09.05', 5, 'Embraer 175'),
          airline('Стокгольм', 'B2 0855', '12.35', 1, 'Embraer 175'),
          airline('Стокгольм', 'B2 0855', '11.05', 7, 'Boeing 737'),
          airline('Москва', 'B2 0983', '06.45', 3, 'Boeing 737'),
          airline('Москва', 'B2 0987', '09.05', 4, 'Embraer 175'),
          airline('Вильнюс', 'B2 0803', '23.05', 1, 'Boeing 737'),
          airline('Хургада', 'B2 0801', '19.05', 2, 'Embraer 175'),
          airline('Барселона', 'B2 0811', '03.05', 6, 'Boeing 737')]
r=0
days=0
r = str(input('Ведите пункт назначения: \n'))
while i < len(flight):
    if flight[i].get_dest() == r:
        InfoOut(i)
    i+=1
i=0
days = int(input('Введите день недели: \n'))
while i < len(flight) :
    if flight[i].get_days() == days :
        InfoOut(i)
    i += 1
